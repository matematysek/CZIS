from industry import IndustrySecondary, TileLocationChecks

# ! machine works is not machine shop eh :)
# see https://en.wikipedia.org/wiki/Edison_Machine_Works

industry = IndustrySecondary(
    id="machine_works",
    accept_cargos_with_input_ratios=[("STAL", 3), ("COPR", 2), ("RFPR", 1), ("STWR", 1), ("PLST", 1)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("POWR", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="166",
    name="string(STR_IND_ELECTRICAL_WORKS)",
    nearby_station_name="string(STR_STATION_DYNAMO)",
    fund_cost_multiplier="120",
)

industry.economy_variations['STEELTOWN'].enabled = True

industry.add_tile(
    id="machine_works_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 70, -31, -39)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 70, -31, -39)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 70, -31, -39)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 70, -31, -39)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 70, -31, -39)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=8,
    zoffset=53,
)

industry.add_spritelayout(
    id="machine_works_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
)
industry.add_spritelayout(
    id="machine_works_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="machine_works_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="machine_works_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="machine_works_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="machine_works_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="machine_works_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)

industry.add_industry_layout(
    id="machine_works_industry_layout_1",
    layout=[
        (0, 0, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (0, 1, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (0, 2, "machine_works_tile_1", "machine_works_spritelayout_5"),
        (0, 3, "machine_works_tile_1", "machine_works_spritelayout_4"),
        (0, 4, "machine_works_tile_1", "machine_works_spritelayout_5"),
        (1, 0, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (1, 1, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (1, 2, "machine_works_tile_1", "machine_works_spritelayout_5"),
        (1, 3, "machine_works_tile_1", "machine_works_spritelayout_4"),
        (1, 4, "machine_works_tile_1", "machine_works_spritelayout_6"),
        (2, 0, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (2, 1, "machine_works_tile_1", "machine_works_spritelayout_1"),
        (2, 2, "machine_works_tile_1", "machine_works_spritelayout_2"),
        (2, 3, "machine_works_tile_1", "machine_works_spritelayout_7"),
        (2, 4, "machine_works_tile_1", "machine_works_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="machine_works_industry_layout_2",
    layout=[
        (0, 2, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (0, 3, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (1, 0, "machine_works_tile_1", "machine_works_spritelayout_1"),
        (1, 1, "machine_works_tile_1", "machine_works_spritelayout_2"),
        (1, 2, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (1, 3, "machine_works_tile_1", "machine_works_spritelayout_3"),
        (2, 0, "machine_works_tile_1", "machine_works_spritelayout_7"),
        (2, 1, "machine_works_tile_1", "machine_works_spritelayout_4"),
        (2, 2, "machine_works_tile_1", "machine_works_spritelayout_4"),
        (2, 3, "machine_works_tile_1", "machine_works_spritelayout_5"),
        (3, 0, "machine_works_tile_1", "machine_works_spritelayout_7"),
        (3, 1, "machine_works_tile_1", "machine_works_spritelayout_5"),
        (3, 2, "machine_works_tile_1", "machine_works_spritelayout_7"),
        (3, 3, "machine_works_tile_1", "machine_works_spritelayout_6"),
    ],
)
