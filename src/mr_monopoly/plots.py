from .tiles import Plot
from .colour import Colour


OLD_KENT_ROAD = Plot(
    name="Old Kent Road",
    colour=Colour.BROWN,
    rent=2,
    rent_with_monopoly=4,
    rent_with_houses=[10, 30, 90, 160],
    rent_with_hotels=[250],
    house_price=50,
    hotel_price=50,
    purchase_price=60,
)

WHITECHAPEL_ROAD = Plot(
    name="Whitechapel Road",
    colour=Colour.BROWN,
    rent=4,
    rent_with_monopoly=8,
    rent_with_houses=[20, 60, 180, 320],
    rent_with_hotels=[450],
    house_price=50,
    hotel_price=50,
    purchase_price=60,
)

THE_ANGEL_ISLINGTON = Plot(
    name="The Angel Islington",
    colour=Colour.LIGHT_BLUE,
    rent=6,
    rent_with_monopoly=12,
    rent_with_houses=[30, 90, 270, 400],
    rent_with_hotels=[550],
    house_price=50,
    hotel_price=50,
    purchase_price=100,
)

EUSTON_ROAD = Plot(
    name="Euston Road",
    colour=Colour.LIGHT_BLUE,
    rent=6,
    rent_with_monopoly=12,
    rent_with_houses=[30, 90, 270, 400],
    rent_with_hotels=[550],
    house_price=50,
    hotel_price=50,
    purchase_price=100,
)

PENTONVILLE_ROAD = Plot(
    name="Pentonville Road",
    colour=Colour.LIGHT_BLUE,
    rent=8,
    rent_with_monopoly=16,
    rent_with_houses=[40, 100, 300, 450],
    rent_with_hotels=[600],
    house_price=50,
    hotel_price=50,
    purchase_price=120,
)

PALL_MALL = Plot(
    name="Pall Mall",
    colour=Colour.PINK,
    rent=10,
    rent_with_monopoly=20,
    rent_with_houses=[50, 150, 450, 625],
    rent_with_hotels=[750],
    house_price=100,
    hotel_price=100,
    purchase_price=140,
)

WHITEHALL = Plot(
    name="Whitehall",
    colour=Colour.PINK,
    rent=10,
    rent_with_monopoly=20,
    rent_with_houses=[50, 150, 450, 625],
    rent_with_hotels=[750],
    house_price=100,
    hotel_price=100,
    purchase_price=140,
)

NORTHUMBERLAND_AVENUE = Plot(
    name="Northumberland Avenue",
    colour=Colour.PINK,
    rent=12,
    rent_with_monopoly=24,
    rent_with_houses=[60, 180, 500, 700],
    rent_with_hotels=[900],
    house_price=100,
    hotel_price=100,
    purchase_price=160,
)

BOW_STREET = Plot(
    name="Bow Street",
    colour=Colour.ORANGE,
    rent=14,
    rent_with_monopoly=28,
    rent_with_houses=[70, 200, 550, 750],
    rent_with_hotels=[950],
    house_price=100,
    hotel_price=100,
    purchase_price=180,
)

MARLBOROUGH_STREET = Plot(
    name="Marlborough Street",
    colour=Colour.ORANGE,
    rent=14,
    rent_with_monopoly=28,
    rent_with_houses=[70, 200, 550, 750],
    rent_with_hotels=[950],
    house_price=100,
    hotel_price=100,
    purchase_price=180,
)

VINE_STREET = Plot(
    name="Vine Street",
    colour=Colour.ORANGE,
    rent=16,
    rent_with_monopoly=32,
    rent_with_houses=[80, 220, 600, 800],
    rent_with_hotels=[1000],
    house_price=100,
    hotel_price=100,
    purchase_price=200,
)

STRAND = Plot(
    name="Strand",
    colour=Colour.RED,
    rent=18,
    rent_with_monopoly=36,
    rent_with_houses=[90, 250, 700, 875],
    rent_with_hotels=[1050],
    house_price=150,
    hotel_price=150,
    purchase_price=220,
)

FLEET_STREET = Plot(
    name="Fleet Street",
    colour=Colour.RED,
    rent=18,
    rent_with_monopoly=36,
    rent_with_houses=[90, 250, 700, 875],
    rent_with_hotels=[1050],
    house_price=150,
    hotel_price=150,
    purchase_price=220,
)

TRAFALGAR_SQUARE = Plot(
    name="Trafalgar Square",
    colour=Colour.RED,
    rent=20,
    rent_with_monopoly=40,
    rent_with_houses=[100, 300, 750, 925],
    rent_with_hotels=[1100],
    house_price=150,
    hotel_price=150,
    purchase_price=240,
)

LEICESTER_SQUARE = Plot(
    name="Leicester Square",
    colour=Colour.YELLOW,
    rent=22,
    rent_with_monopoly=44,
    rent_with_houses=[110, 330, 800, 975],
    rent_with_hotels=[1150],
    house_price=150,
    hotel_price=150,
    purchase_price=260,
)

COVENTRY_STREET = Plot(
    name="Coventry Street",
    colour=Colour.YELLOW,
    rent=22,
    rent_with_monopoly=44,
    rent_with_houses=[110, 330, 800, 975],
    rent_with_hotels=[1150],
    house_price=150,
    hotel_price=150,
    purchase_price=260,
)

PICCADILLY = Plot(
    name="Piccadilly",
    colour=Colour.YELLOW,
    rent=24,
    rent_with_monopoly=48,
    rent_with_houses=[120, 360, 850, 1025],
    rent_with_hotels=[1200],
    house_price=150,
    hotel_price=150,
    purchase_price=280,
)

REGENT_STREET = Plot(
    name="Regent Street",
    colour=Colour.GREEN,
    rent=26,
    rent_with_monopoly=52,
    rent_with_houses=[130, 390, 900, 1100],
    rent_with_hotels=[1275],
    house_price=200,
    hotel_price=200,
    purchase_price=300,
)

OXFORD_STREET = Plot(
    name="Oxford Street",
    colour=Colour.GREEN,
    rent=26,
    rent_with_monopoly=52,
    rent_with_houses=[130, 390, 900, 1100],
    rent_with_hotels=[1275],
    house_price=200,
    hotel_price=200,
    purchase_price=300,
)

BOND_STREET = Plot(
    name="Bond Street",
    colour=Colour.GREEN,
    rent=28,
    rent_with_monopoly=56,
    rent_with_houses=[150, 450, 1000, 1200],
    rent_with_hotels=[1400],
    house_price=200,
    hotel_price=200,
    purchase_price=320,
)

PARK_LANE = Plot(
    name="Park Lane",
    colour=Colour.DARK_BLUE,
    rent=35,
    rent_with_monopoly=70,
    rent_with_houses=[175, 500, 1100, 1300],
    rent_with_hotels=[1500],
    house_price=200,
    hotel_price=200,
    purchase_price=350,
)

MAYFAIR = Plot(
    name="Mayfair",
    colour=Colour.DARK_BLUE,
    rent=50,
    rent_with_monopoly=100,
    rent_with_houses=[200, 600, 1400, 1700],
    rent_with_hotels=[2000],
    house_price=200,
    hotel_price=200,
    purchase_price=400,
)
