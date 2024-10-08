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


costVect = [MaterialCost.Fe.value, MaterialCost.Si.value, MaterialCost.Co.value, MaterialCost.Gr.value,
            MaterialCost.Ni.value, MaterialCost.Ag.value, MaterialCost.Au.value, MaterialCost.Pt.value]


def fuel_mass(fuel_type):
    switch = {
        'Hydrogen': 2,
        'Deuterium': 4,
        'Atmospheric': 1,
        'Ion': .5
    }

    return switch.get(fuel_type, 0)
