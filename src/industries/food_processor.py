from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="food_processor",
    accept_cargos_with_input_ratios=[("BEAN", 6), ("FRUT", 6), ("ELEC", 1), ("PACK", 1)],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[("FOOD", 8)],
    prob_in_game="3",
    prob_map_gen="5",
    map_colour="181",
    location_checks=dict(
        near_at_least_one_of_these_keystone_industries=[
            ["arable_farm", "fruit_plantation", "coffee_estate", "vineyard"],
            72,
        ]
    ),
    name="string(STR_IND_CANNERY)",
    nearby_station_name="string(STR_STATION_CANNERY)",
    fund_cost_multiplier="65",
)

industry.economy_variations["BASIC_TROPIC"].enabled = True

industry.economy_variations["IN_A_HOT_COUNTRY"].enabled = True
industry.economy_variations["IN_A_HOT_COUNTRY"].accept_cargos_with_input_ratios = [
    ("NUTS", 6),
    ("FRUT", 6),
]
industry.economy_variations["IN_A_HOT_COUNTRY"].prod_cargo_types_with_output_ratios = [
    ("EOIL", 4),
    ("FOOD", 4),
]

industry.economy_variations["STEELTOWN"].enabled = True
industry.economy_variations["STEELTOWN"].accept_cargos_with_input_ratios = [
    ("STSE", 2),
    ("FISH", 2),
    ("SALT", 2),
    ("FRUT", 2),
]

industry.add_tile(
    id="food_processor_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(type="concrete")
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 10, 64, 87, -31, -56)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 10, 64, 87, -31, -56)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 10, 64, 87, -31, -56)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 10, 64, 87, -31, -56)],
)

industry.add_spritelayout(
    id="food_processor_spritelayout_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
)
industry.add_spritelayout(
    id="food_processor_spritelayout_2",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
)
industry.add_spritelayout(
    id="food_processor_spritelayout_3",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
)
industry.add_spritelayout(
    id="food_processor_spritelayout_4",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
)

industry.add_industry_layout(
    id="food_processor_industry_layout_1",
    layout=[
        (0, 0, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (0, 1, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (0, 2, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (1, 0, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (1, 1, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (1, 2, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (2, 0, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (2, 1, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (2, 2, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (3, 0, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (3, 1, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (3, 2, "food_processor_tile_1", "food_processor_spritelayout_4"),
    ],
)
industry.add_industry_layout(
    id="food_processor_industry_layout_2",
    layout=[
        (0, 0, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (0, 1, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (0, 2, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (0, 3, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (1, 0, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (1, 1, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (1, 2, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (1, 3, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (2, 0, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (2, 1, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (2, 2, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (3, 0, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (3, 1, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (3, 2, "food_processor_tile_1", "food_processor_spritelayout_1"),
    ],
)
industry.add_industry_layout(
    id="food_processor_industry_layout_3",
    layout=[
        (0, 0, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (0, 1, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (0, 2, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (0, 3, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (1, 0, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (1, 1, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (1, 2, "food_processor_tile_1", "food_processor_spritelayout_2"),
        (1, 3, "food_processor_tile_1", "food_processor_spritelayout_3"),
        (2, 0, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (2, 1, "food_processor_tile_1", "food_processor_spritelayout_1"),
        (2, 2, "food_processor_tile_1", "food_processor_spritelayout_4"),
        (2, 3, "food_processor_tile_1", "food_processor_spritelayout_4"),
    ],
)
