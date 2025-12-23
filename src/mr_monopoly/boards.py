from .board import Board
from .tiles import *
from .plots import *


KINGS_CROSS = Station(
    name="Kings Cross Station", rent=[25, 50, 100, 200], purchase_price=200
)

# Stations are identical in every way except name
MARLEYBONE = Station.rename("Marleybone Station", KINGS_CROSS)
FENCHURCH_ST = Station.rename("Fenchurch St. Station", KINGS_CROSS)
LIVERPOOL_ST = Station.rename("Liverpool St. Station", KINGS_CROSS)


CLASSIC_UK = Board(
    tiles=Tiles(
        tiles=[
            Go(),
            OLD_KENT_ROAD,
            WHITECHAPEL_ROAD,
            Tax(amount=200),
            KINGS_CROSS,
            THE_ANGEL_ISLINGTON,
            EUSTON_ROAD,
            PENTONVILLE_ROAD,
            Jail(),
            PALL_MALL,
            Utilities(
                type=UtilityType.ELECTRIC_COMPANY,
                rent_multiplier=[4, 10],
                purchase_price=150,
            ),
            WHITEHALL,
            NORTHUMBERLAND_AVENUE,
            MARLEYBONE,
            BOW_STREET,
            MARLBOROUGH_STREET,
            VINE_STREET,
            FreeParking(),
            STRAND,
            FLEET_STREET,
            TRAFALGAR_SQUARE,
            FENCHURCH_ST,
            LEICESTER_SQUARE,
            COVENTRY_STREET,
            Utilities(
                type=UtilityType.WATER_WORKS,
                rent_multiplier=[4, 10],
                purchase_price=150,
            ),
            PICCADILLY,
            GoToJail(),
            REGENT_STREET,
            OXFORD_STREET,
            BOND_STREET,
            LIVERPOOL_ST,
            PARK_LANE,
            Tax(amount=100),
            MAYFAIR,
        ]
    )
)
