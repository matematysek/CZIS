from cargo import Cargo

cargo = Cargo(
    id="packaging",
    type_name="STR_PACK",
    unit_name="STR_UNIT_PACK",
    type_abbreviation="string(STR_CID_PACK)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE)",
    cargo_label="GOOD",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_CRATES",
    items_of_cargo="TTD_STR_QUANTITY_GOODS",
    penalty_lowerbound="10",
    single_penalty_length="56",
    price_factor=169,
    capacity_multiplier="2",
    icon_indices=(5, 0),
    sprites_complete=True,
)
