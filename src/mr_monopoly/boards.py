from .board import Board
from .tiles import Go, Jail, Tax, GoToJail
from .plots import *


CLASSIC_UK = Board(
    tiles=[
        Go(),
        OLD_KENT_ROAD,
        WHITECHAPEL_ROAD,
        Tax(amount=200),
        THE_ANGEL_ISLINGTON,
        EUSTON_ROAD,
        PENTONVILLE_ROAD,
        Jail(),
        PALL_MALL,
        WHITEHALL,
        NORTHUMBERLAND_AVENUE,
        BOW_STREET,
        MARLBOROUGH_STREET,
        VINE_STREET,
        STRAND,
        FLEET_STREET,
        TRAFALGAR_SQUARE,
        LEICESTER_SQUARE,
        COVENTRY_STREET,
        PICCADILLY,
        GoToJail(),
        REGENT_STREET,
        OXFORD_STREET,
        BOND_STREET,
        PARK_LANE,
        Tax(amount=100),
        MAYFAIR,
    ]
)
