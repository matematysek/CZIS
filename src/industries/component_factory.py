from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="component_factory",
    accept_cargos_with_input_ratios=[
        ("STSE", 2),
        ("PLAS", 2),
        ("STAL", 2),
        ("POWR", 2),
        ("ELEC", 2),
    ],
    prod_cargo_types_with_output_ratios=[("VPTS", 8)],
    prob_in_game="7",
    prob_map_gen="8",
    map_colour="166",
    name="string(STR_IND_COMPONENT_FACTORY)",
    nearby_station_name="string(STR_STATION_COMPONENTS)",
    fund_cost_multiplier="95",
    pollution_and_squalor_factor=1,
)

industry.economy_variations["CZ"].enabled = True


industry.add_tile(
    id="component_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 100, -31, -66)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 100, -31, -66)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 100, -31, -66)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -20)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)

industry.add_spritelayout(
    id="component_factory_spritelayout_large_building_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_large_building_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_large_building_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[
        spriteset_6
    ],  # out of order spriteset number, due to historical crap, can fix by tidying spritesheet
)

industry.add_industry_layout(
    id="component_factory_industry_layout_1",
    layout=[
        (
            0,
            0,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_2",
        ),
        (
            0,
            1,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_3",
        ),
        (
            0,
            2,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_2",
        ),
        (
            0,
            3,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_3",
        ),
        (
            0,
            4,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_3",
        ),
        (
            1,
            0,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_1",
        ),
        (1, 1, "component_factory_tile_1", "component_factory_spritelayout_4"),
        (1, 2, "component_factory_tile_1", "component_factory_spritelayout_5"),
        (1, 3, "component_factory_tile_1", "component_factory_spritelayout_4"),
        (1, 4, "component_factory_tile_1", "component_factory_spritelayout_4"),
        (
            2,
            0,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_2",
        ),
        (
            2,
            1,
            "component_factory_tile_1",
            "component_factory_spritelayout_large_building_3",
        ),
        (2, 2, "component_factory_tile_1", "component_factory_spritelayout_5"),
        (2, 3, "component_factory_tile_1", "component_factory_spritelayout_5"),
        (2, 4, "component_factory_tile_1", "component_factory_spritelayout_5"),
    ],
)
