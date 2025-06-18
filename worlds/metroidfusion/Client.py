import logging
from collections import deque
from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient
from .data import memory
from .data.minor_locations import location_order as minor_location_order
from .data.major_locations import location_order as major_location_order

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext


logger = logging.getLogger("Client")


def get_byte_bit_from_index(index):
    return index // 8, 2 ** (index % 8)

def get_bit_value_from_position(position):
    return 2 ** position


class MetroidFusionClient(BizHawkClient):
    game = "Metroid Fusion"
    system = "GBA"
    patch_suffix = ".apmetfus"

    def __init__(self) -> None:
        self.ewram = "EWRAM"
        self.iwram = "IWRAM"
        self.sram = "SRAM"
        self.bus = "System Bus"
        self.rom = "ROM"
        self.location_name_to_id: dict[str, int] | None = None

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name = ((await bizhawk.read(ctx.bizhawk_ctx, [(memory.rom_name_location, 20, self.rom)]))[0])
            rom_name = rom_name.decode("utf-8")
            if rom_name[:3] != "MFU":
                return False  # Not a Final Fantasy 1 ROM
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True

        return True

    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        import base64
        auth_raw = (await bizhawk.read(
            ctx.bizhawk_ctx,
            [(memory.rom_name_location, 20, self.rom)]))[0]
        ctx.auth = base64.b64encode(auth_raw).decode()

    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ctx.server is None:
            return

        if ctx.slot is None:
            return
        try:
            if self.location_name_to_id is None:
                from . import MetroidFusionWorld
                self.location_name_to_id = MetroidFusionWorld.location_name_to_id
            await self.check_victory(ctx)
            await self.location_check(ctx)
            await self.received_items_check(ctx)
            await self.sync_upgrades(ctx)
        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass

    async def location_check(self, ctx: "BizHawkClientContext"):
        locations_checked = []

        # Minor locations
        locations_data = await self.read_ram_values_guarded(ctx, memory.minor_locations_start, 16, self.ewram)
        if locations_data is None:
            return
        for index, location in enumerate(minor_location_order):
            location_byte, location_bit = get_byte_bit_from_index(index)
            if (int(locations_data[location_byte]) & location_bit) > 0:
                locations_checked.append(self.location_name_to_id[location])

        # Major locations
        locations_data = await self.read_ram_values_guarded(ctx, memory.major_locations_start, 4, self.iwram)
        if locations_data is None:
            return
        for index, location in enumerate(major_location_order):
            if location == "ARC Data Room 2 -- Unused":
                continue
            location_byte, location_bit = get_byte_bit_from_index(index)
            if (int(locations_data[location_byte]) & location_bit) > 0:
                locations_checked.append(self.location_name_to_id[location])

        found_locations = await ctx.check_locations(locations_checked)
        for location in found_locations:
            ctx.locations_checked.add(location)
            location_name = ctx.location_names.lookup_in_game(location)
            logger.info(
                f'New Check: {location_name} ({len(ctx.locations_checked)}/'
                f'{len(ctx.missing_locations) + len(ctx.checked_locations)})')

    async def received_items_check(self, ctx: "BizHawkClientContext"):
        write_list: list[tuple[int, list[int], str]] = []

        items_received_count_low = await self.read_ram_value_guarded(ctx, memory.items_received_low, self.bus)
        items_received_count_high = await self.read_ram_value_guarded(ctx, memory.items_received_high, self.bus)
        if items_received_count_low is None or items_received_count_high is None:
            return
        items_received_count = int.from_bytes([items_received_count_low, items_received_count_high], "little")
        if items_received_count == 0xFFFF:
            items_received_count = 0
        if items_received_count < len(ctx.items_received):
            current_item = ctx.items_received[items_received_count]
            current_item_id = current_item.item
            current_item_name = ctx.item_names.lookup_in_game(current_item_id, ctx.game)
            if current_item.player == ctx.slot and current_item.location >= 0:
                pass
            elif current_item_name == "Infant Metroid":
                metroid_count_data = await self.read_ram_value_guarded(ctx,
                                                                       memory.FusionInfantMetroid.current_address,
                                                                       self.iwram)
                if metroid_count_data is None:
                    return
                new_count = metroid_count_data + 1
                write_list.append((memory.FusionInfantMetroid.current_address, [new_count], self.iwram))
            elif current_item_name in memory.keycards.keys():
                keycard = memory.keycards[current_item_name]
                current_keycard_data = await self.read_ram_value_guarded(ctx, keycard.address, self.iwram)
                if current_keycard_data is None:
                    return
                new_keycard_value = current_keycard_data | get_bit_value_from_position(keycard.bit)
                write_list.append((keycard.address, [new_keycard_value], self.iwram))
            elif current_item_name in memory.upgrades.keys():
                upgrade = memory.upgrades[current_item_name]
                current_upgrade_obtained_data = await self.read_ram_value_guarded(ctx, upgrade.inventory_address, self.iwram)
                current_upgrade_toggled_data = await self.read_ram_value_guarded(ctx, upgrade.toggled_address, self.iwram)
                if current_upgrade_obtained_data is None or current_upgrade_toggled_data is None:
                    return
                inv_bit = get_bit_value_from_position(upgrade.inventory_bit)
                new_obtained_value = current_upgrade_obtained_data | inv_bit
                write_list.append((upgrade.inventory_address, [new_obtained_value], self.iwram))
                up_bit = get_bit_value_from_position(upgrade.toggled_bit)
                new_toggled_value = current_upgrade_toggled_data | up_bit
                write_list.append((upgrade.toggled_address, [new_toggled_value], self.iwram))
            elif current_item_name in memory.tanks.keys():
                tank = memory.tanks[current_item_name]
                if current_item_name == "Power Bomb Tank":
                    current_amount_data = await self.read_ram_value_guarded(ctx, tank.current_address, self.iwram)
                    max_amount_data = await self.read_ram_value_guarded(ctx, tank.max_address, self.iwram)
                    if current_amount_data is None or max_amount_data is None:
                        return
                    current_amount = current_amount_data
                    max_amount = max_amount_data
                    write_list.append((tank.current_address, [current_amount + tank.tank_size], self.iwram))
                    write_list.append((tank.max_address, [max_amount + tank.tank_size], self.iwram))
                elif current_item_name == "Energy Tank":
                    current_amount_data = await self.read_ram_values_guarded(ctx, tank.current_address, 2, self.iwram)
                    max_amount_data = await self.read_ram_values_guarded(ctx, tank.max_address, 2, self.iwram)
                    if current_amount_data is None or max_amount_data is None:
                        return
                    max_amount = int.from_bytes(max_amount_data, "little")
                    write_list.append((tank.current_address, [(max_amount + tank.tank_size) % 256], self.iwram))
                    write_list.append((tank.max_address, [(max_amount + tank.tank_size) % 256], self.iwram))
                    write_list.append((tank.current_address + 1, [(max_amount + tank.tank_size) // 256], self.iwram))
                    write_list.append((tank.max_address + 1, [(max_amount + tank.tank_size) // 256], self.iwram))
                else:
                    current_amount_data = await self.read_ram_values_guarded(ctx, tank.current_address, 2, self.iwram)
                    max_amount_data = await self.read_ram_values_guarded(ctx, tank.max_address, 2, self.iwram)
                    if current_amount_data is None or max_amount_data is None:
                        return
                    current_amount = int.from_bytes(current_amount_data, "little")
                    max_amount = int.from_bytes(max_amount_data, "little")
                    write_list.append((tank.current_address, [current_amount + tank.tank_size], self.iwram))
                    write_list.append((tank.max_address, [max_amount + tank.tank_size], self.iwram))

            items_received_count += 1
            write_list.append((memory.items_received_low, [items_received_count % 256], self.bus))
            write_list.append((memory.items_received_high, [items_received_count // 256], self.bus))
            write_successful = await self.write_ram_values_guarded(ctx, write_list)
            if write_successful:
                if current_item.player != ctx.slot or current_item.location == 0:
                    await bizhawk.display_message(ctx.bizhawk_ctx, f"Received {current_item_name}")


    async def check_victory(self, ctx):
        value = await bizhawk.read(ctx.bizhawk_ctx, [(memory.game_mode, 1, self.iwram)])
        if value is None or ctx.finished_game:
            return
        else:
            if int.from_bytes(value[0]) == memory.credits_mode:
                await ctx.send_msgs([
                    {"cmd": "StatusUpdate",
                     "status": ClientStatus.CLIENT_GOAL}
                ])
                ctx.finished_game = True

    async def sync_upgrades(self, ctx: "BizHawkClientContext"):
        missile_max = 10
        energy_max = 99
        power_bomb_max = 10
        infant_metroid_count = 0
        write_list: list[tuple[int, list[int], str]] = []
        upgrade_addresses = {}
        keycard_value = 0x01
        items_received_count_low = await self.read_ram_value_guarded(ctx, memory.items_received_low, self.bus)
        items_received_count_high = await self.read_ram_value_guarded(ctx, memory.items_received_high, self.bus)
        if items_received_count_low is None or items_received_count_high is None:
            return
        items_received_count = int.from_bytes([items_received_count_low, items_received_count_high], "little")
        if items_received_count == 0xFFFF:
            items_received_count = 0
        if items_received_count >= len(ctx.items_received):
            for item in ctx.items_received:
                current_item_id = item.item
                current_item_name = ctx.item_names.lookup_in_game(current_item_id, ctx.game)
                if current_item_name == "Infant Metroid":
                    infant_metroid_count += 1
                elif current_item_name in memory.upgrades.keys():
                    upgrade = memory.upgrades[current_item_name]
                    inv_bit = get_bit_value_from_position(upgrade.inventory_bit)
                    if upgrade.inventory_address in upgrade_addresses.keys():
                        current_upgrade_data = upgrade_addresses[upgrade.inventory_address]
                        new_upgrade_value = current_upgrade_data | inv_bit
                        upgrade_addresses[upgrade.inventory_address] = new_upgrade_value
                    else:
                        current_upgrade_data = await self.read_ram_value_guarded(ctx, upgrade.inventory_address, self.iwram)
                        if current_upgrade_data is None:
                            return
                        new_upgrade_value = current_upgrade_data | inv_bit
                        upgrade_addresses[upgrade.inventory_address] = new_upgrade_value
                elif current_item_name in memory.tanks.keys():
                    if current_item_name == "Missile Tank":
                        missile_max += memory.tanks[current_item_name].tank_size
                    elif current_item_name == "Energy Tank":
                        energy_max += memory.tanks[current_item_name].tank_size
                    elif current_item_name == "Power Bomb Tank":
                        power_bomb_max += memory.tanks[current_item_name].tank_size
                elif current_item_name in memory.keycards.keys():
                    keycard = memory.keycards[current_item_name]
                    current_keycard_data = await self.read_ram_value_guarded(ctx, keycard.address, self.iwram)
                    if current_keycard_data is None:
                        return
                    keycard_value = keycard_value | get_bit_value_from_position(keycard.bit)
                    write_list.append((keycard.address, [keycard_value], self.iwram))
                    write_list.append((memory.keycard_flash_address, [keycard_value], self.iwram))
            for address, value in upgrade_addresses.items():
                write_list.append((address, [value], self.iwram))
            write_list.append((memory.FusionInfantMetroid.current_address, [infant_metroid_count], self.iwram))
            write_list.append((memory.tanks["Missile Tank"].max_address, [missile_max], self.iwram))
            write_list.append((memory.tanks["Energy Tank"].max_address, [energy_max % 256], self.iwram))
            write_list.append((memory.tanks["Energy Tank"].max_address + 1, [energy_max // 256], self.iwram))
            write_list.append((memory.tanks["Power Bomb Tank"].max_address, [power_bomb_max], self.iwram))
            await self.write_ram_values_guarded(ctx, write_list)


    async def read_ram_values_guarded(self, ctx: "BizHawkClientContext", location: int, size: int, domain: str):
        value = await bizhawk.guarded_read(ctx.bizhawk_ctx,
                                           [(location, size, domain)],
                                           [(memory.game_mode, [memory.ingame_mode], self.iwram)])
        if value is None:
            return None
        return value[0]

    async def read_ram_value_guarded(self, ctx: "BizHawkClientContext", location: int, domain: str):
        value = await bizhawk.guarded_read(ctx.bizhawk_ctx,
                                           [(location, 1, domain)],
                                           [(memory.game_mode, [memory.ingame_mode], self.iwram)])
        if value is None:
            return None
        return int.from_bytes(value[0], "little")


    async def write_ram_values_guarded(self, ctx: "BizHawkClientContext", write_list):
        return await bizhawk.guarded_write(ctx.bizhawk_ctx,
                                           write_list,
                                           [(memory.game_mode, [memory.ingame_mode], self.iwram)])