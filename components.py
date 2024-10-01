from enum import Enum


class GridSize(Enum):
    SMALL = 1
    LARGE = 2


class MaterialCost(Enum):
    Fe = 156
    Si = 256
    Co = 1578
    Gr = 52
    Ni = 315
    Ag = 2658
    Au = 21516
    Pt = 92111
