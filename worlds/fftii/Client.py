import logging
import time
from typing import TYPE_CHECKING

from NetUtils import ClientStatus

import worlds._bizhawk as bizhawk
from settings import get_settings
from worlds._bizhawk.client import BizHawkClient

from .data import memory
from .data.items import item_data_lookup, gear_item_names, gil_item_names, gil_item_sizes

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

logger = logging.getLogger("Client")

guard_list = [
    (memory.world_loaded_address, [memory.world_loaded_value[3]], "MainRAM"),
    (memory.world_loaded_address + 1, [memory.world_loaded_value[2]], "MainRAM"),
    (memory.world_loaded_address + 2, [memory.world_loaded_value[1]], "MainRAM"),
    (memory.world_loaded_address + 3, [memory.world_loaded_value[0]], "MainRAM"),
]

def get_byte_bit_from_index(index):
    return index // 8, 2 ** (index % 8)

def get_bit_value_from_position(position):
    return 2 ** position

class FinalFantasyTacticsIvaliceIslandClient(BizHawkClient):
    game = "Final Fantasy Tactics Ivalice Island"
    system = "PSX"
    patch_suffix = ".apfftii"

    def __init__(self) -> None:
        self.ram = "MainRAM"
        self.location_name_to_id: dict[str, int] | None = None
        self.logged_version = False

    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        try:
            # Check ROM name/patch version
            rom_name = ((await bizhawk.read(
                ctx.bizhawk_ctx,
                [(memory.cd_name_location, len(memory.cd_name), self.ram)]))[0])
            try:
                rom_name = rom_name.decode("utf-8")
            except UnicodeDecodeError:
                return False
            if rom_name != memory.cd_name:
                return False  # Not a Metroid Fusion ROM
        except bizhawk.RequestFailedError:
            return False  # Not able to get a response, say no for now

        ctx.game = self.game
        ctx.items_handling = 0b111
        ctx.want_slot_data = True
        return True

    async def set_auth2(self, ctx: "BizHawkClientContext") -> None:
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
                from . import FinalFantasyTacticsIvaliceIslandWorld
                self.location_name_to_id = FinalFantasyTacticsIvaliceIslandWorld.location_name_to_id
            await self.check_victory(ctx)
            await self.location_check(ctx)
            await self.received_items_check(ctx)

        except bizhawk.RequestFailedError:
            # The connector didn't respond. Exit handler and return to main loop to reconnect
            pass

    async def location_check(self, ctx: "BizHawkClientContext"):
        pass
        # locations_checked = []
        #
        #
        # # Minor locations
        # locations_data = await self.read_ram_values_guarded(ctx, memory.minor_locations_start, 16, self.ewram)
        # if locations_data is None:
        #     return
        # for index, location in enumerate(minor_location_order):
        #     location_byte, location_bit = get_byte_bit_from_index(index)
        #     if (int(locations_data[location_byte]) & location_bit) > 0:
        #         locations_checked.append(self.location_name_to_id[location])
        #
        # found_locations = await ctx.check_locations(locations_checked)
        # for location in found_locations:
        #     ctx.locations_checked.add(location)
        #     location_name = ctx.location_names.lookup_in_game(location)
        #     if self.display_location_found_messages:
        #         logger.info(
        #             f'New Check: {location_name} ({len(ctx.locations_checked)}/'
        #             f'{len(ctx.missing_locations) + len(ctx.checked_locations)})')

    async def received_items_check(self, ctx: "BizHawkClientContext"):
        write_list: list[tuple[int, list[int], str]] = []

        items_received_count_low = await self.read_ram_value_guarded(ctx, memory.items_received_low)
        items_received_count_high = await self.read_ram_value_guarded(ctx, memory.items_received_high)
        if items_received_count_low is None or items_received_count_high is None:
            return
        items_received_count = int.from_bytes([items_received_count_low, items_received_count_high], "little")
        if items_received_count < len(ctx.items_received):
            current_item = ctx.items_received[items_received_count]
            current_item_id = current_item.item
            current_item_name = ctx.item_names.lookup_in_game(current_item_id, ctx.game)
            if current_item_name in gear_item_names:
                write_list_candidate = await self.write_inventory_item(ctx, current_item_name)
                if write_list_candidate is None:
                    return
                write_list.append(write_list_candidate)
            elif current_item_name == "Progressive Shop Level":
                write_list_candidate = await self.increment_shop_progression(ctx)
                if write_list_candidate is None:
                    return
                write_list.append(write_list_candidate)
            elif current_item_name in gil_item_names:
                write_list_candidate = await self.write_gil_item(ctx, current_item_name)
                if write_list_candidate is None:
                    return
                write_list.extend(write_list_candidate)
            items_received_count += 1
            write_list.append((memory.items_received_low, [items_received_count % 256], self.ram))
            write_list.append((memory.items_received_high, [items_received_count // 256], self.ram))
            write_successful = await self.write_ram_values_guarded(ctx, write_list)
            if write_successful:
                await bizhawk.display_message(ctx.bizhawk_ctx, f"Received {current_item_name}")


    async def check_victory(self, ctx):
        value = None
        if value is None or ctx.finished_game:
            return
        else:
            if int.from_bytes(value[0]) == 0:
                await ctx.send_msgs([
                    {"cmd": "StatusUpdate",
                     "status": ClientStatus.CLIENT_GOAL}
                ])
                ctx.finished_game = True

    async def write_inventory_item(self, ctx: "BizHawkClientContext", item: str) -> tuple[int, list[int], str] | None:
        item_index = item_data_lookup[item].game_id
        current_item_data = await self.read_ram_value_guarded(ctx, memory.inventory_start_address + item_index)
        if current_item_data is None:
            return
        current_item_quantity = current_item_data
        new_item_quantity = min(99, current_item_quantity + 1)
        return (memory.inventory_start_address + item_index, [new_item_quantity], self.ram)

    async def increment_shop_progression(self, ctx: "BizHawkClientContext") -> tuple[int, list[int], str] | None:
        current_shop_data = await self.read_ram_value_guarded(ctx, memory.shop_progression_address)
        if current_shop_data is None:
            return
        new_shop_progression = min(15, current_shop_data + 1)
        return (memory.shop_progression_address, [new_shop_progression], self.ram)

    async def write_gil_item(self, ctx: "BizHawkClientContext", gil_item) -> list[tuple[int, list[int], str]] | None:
        current_gil_data = await self.read_ram_values_guarded(ctx, memory.war_funds_address, memory.war_funds_length)
        if current_gil_data is None:
            return None
        current_gil = int.from_bytes(current_gil_data, "little")
        slot_data = ctx.slot_data
        gil_item_size = int(ctx.slot_data["gil_item_size"])
        gil_quantity = gil_item_sizes[gil_item_size][gil_item]
        new_gil = min(99999999, current_gil + gil_quantity)
        return [
            (memory.war_funds_address, [new_gil % 256], self.ram),
            (memory.war_funds_address + 1, [new_gil // 256 % 256], self.ram),
            (memory.war_funds_address + 2, [new_gil // (2**16) % 256], self.ram),
            (memory.war_funds_address + 3, [new_gil // (2**24)], self.ram),
        ]

    async def read_ram_values_guarded(self, ctx: "BizHawkClientContext", location: int, size: int):
        value = await bizhawk.guarded_read(ctx.bizhawk_ctx, [(location, size, self.ram)], guard_list)
        if value is None:
            return None
        return value[0]

    async def read_ram_value_guarded(self, ctx: "BizHawkClientContext", location: int):
        value = await bizhawk.guarded_read(ctx.bizhawk_ctx, [(location, 1, self.ram)], guard_list)
        if value is None:
            return None
        return int.from_bytes(value[0], "little")

    async def write_ram_values_guarded(self, ctx: "BizHawkClientContext", write_list):
        return await bizhawk.guarded_write(ctx.bizhawk_ctx, write_list, guard_list)
