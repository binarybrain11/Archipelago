from .logic.FFTRegion import FFTRegion
from .logic.regions.Fovoham import fovoham_regions
from .logic.regions.Gallione import gallione_regions
from .logic.regions.Jobs import jobs_regions
from .logic.regions.Lesalia import lesalia_regions
from .logic.regions.Limberry import limberry_regions
from .logic.regions.Lionel import lionel_regions
from .logic.regions.Murond import murond_regions
from .logic.regions.Zeltennia import zeltennia_regions

world_map_regions: list[FFTRegion] = [
    *gallione_regions,
    *fovoham_regions,
    *lesalia_regions,
    *lionel_regions,
    *zeltennia_regions,
    *limberry_regions,
    *murond_regions
]

menu_regions: list[FFTRegion] = [
    *jobs_regions
]

all_regions: list[FFTRegion] = [
    *world_map_regions, *menu_regions
]