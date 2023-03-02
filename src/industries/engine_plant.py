from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="engine_plant",
    accept_cargos_with_input_ratios=[("STEL", 2), ("ALUM", 2), ("TYRE", 2), ("RFPR", 2), ('ELEC', 2)],
    prod_cargo_types_with_output_ratios=[
        ("VENG", 8)
    ],  # high engine plant production is unwanted as there is only one output cargo
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="45",
    name="string(STR_IND_ENGINE_PLANT)",
    nearby_station_name="string(STR_STATION_POWERTRAIN)",
    fund_cost_multiplier="120",
    pollution_and_squalor_factor=1,
)
industry.economy_variations["CZ"].enabled = True

industry.add_tile(
    id="engine_plant_tile_1",
    animation_length=47,
    animation_looping=True,
    animation_speed=2,
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="cobble",
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
sprite_smoke = industry.add_smoke_sprite(
    smoke_type="dark_smoke_small",
    xoffset=0,
    yoffset=8,
    zoffset=53,
)

industry.add_spritelayout(
    id="engine_plant_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    smoke_sprites=[sprite_smoke],
)
industry.add_spritelayout(
    id="engine_plant_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="engine_plant_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="engine_plant_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)
industry.add_spritelayout(
    id="engine_plant_spritelayout_5",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_5],
)
industry.add_spritelayout(
    id="engine_plant_spritelayout_6",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_6],
)
industry.add_spritelayout(
    id="engine_plant_spritelayout_7",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_7],
)

industry.add_industry_layout(
    id="engine_plant_industry_layout_1",
    layout=[
        (0, 0, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (0, 1, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (0, 2, "engine_plant_tile_1", "engine_plant_spritelayout_5"),
        (0, 3, "engine_plant_tile_1", "engine_plant_spritelayout_4"),
        (0, 4, "engine_plant_tile_1", "engine_plant_spritelayout_5"),
        (1, 0, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (1, 1, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (1, 2, "engine_plant_tile_1", "engine_plant_spritelayout_5"),
        (1, 3, "engine_plant_tile_1", "engine_plant_spritelayout_4"),
        (1, 4, "engine_plant_tile_1", "engine_plant_spritelayout_6"),
        (2, 0, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (2, 1, "engine_plant_tile_1", "engine_plant_spritelayout_1"),
        (2, 2, "engine_plant_tile_1", "engine_plant_spritelayout_2"),
        (2, 3, "engine_plant_tile_1", "engine_plant_spritelayout_7"),
        (2, 4, "engine_plant_tile_1", "engine_plant_spritelayout_7"),
    ],
)
industry.add_industry_layout(
    id="engine_plant_industry_layout_2",
    layout=[
        (0, 2, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (0, 3, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (1, 0, "engine_plant_tile_1", "engine_plant_spritelayout_1"),
        (1, 1, "engine_plant_tile_1", "engine_plant_spritelayout_2"),
        (1, 2, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (1, 3, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
        (2, 0, "engine_plant_tile_1", "engine_plant_spritelayout_4"),
        (2, 1, "engine_plant_tile_1", "engine_plant_spritelayout_7"),
        (2, 2, "engine_plant_tile_1", "engine_plant_spritelayout_6"),
        (2, 3, "engine_plant_tile_1", "engine_plant_spritelayout_6"),
        (3, 0, "engine_plant_tile_1", "engine_plant_spritelayout_4"),
        (3, 1, "engine_plant_tile_1", "engine_plant_spritelayout_5"),
        (3, 2, "engine_plant_tile_1", "engine_plant_spritelayout_4"),
        (3, 3, "engine_plant_tile_1", "engine_plant_spritelayout_3"),
    ],
)
