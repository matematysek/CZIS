rom cargo import Cargo

cargo = Cargo(
    id="electricity",
    type_name="STR_ELECTRICITY",
    unit_name="STR_ELECTRICITY",
    type_abbreviation="string(STR_CID_ELECTRICITY)",
    sprite="NEW_CARGO_SPRITE",
    weight="0.5",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE)",
    cargo_label="ELEC",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_BATTERIES",
    items_of_cargo="TTD_STR_QUANTITY_BATTERIES",
    penalty_lowerbound="10",
    single_penalty_length="56",
    price_factor=169,
    capacity_multiplier="2",
    icon_indices=(5, 0),
    sprites_complete=True,
)
