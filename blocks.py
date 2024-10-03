from components import GridSize
import numpy as np
from components import MaterialCost

costVect = [MaterialCost.Fe.value, MaterialCost.Si.value, MaterialCost.Co.value, MaterialCost.Gr.value,
                 MaterialCost.Ni.value, MaterialCost.Ag.value, MaterialCost.Au.value, MaterialCost.Pt.value]

def calculate_cost(materialList):
    cost = np.dot(materialList, costVect)
    return cost


class PowerPlant:
    def __init__(self, name):
        self.name = name


class Part:
    cost_vect = [MaterialCost.Fe.value, MaterialCost.Si.value, MaterialCost.Co.value, MaterialCost.Gr.value,
                 MaterialCost.Ni.value, MaterialCost.Ag.value, MaterialCost.Au.value, MaterialCost.Pt.value]

    def __init__(self, name, mat_vect):
        self.name = name
        self.matVect = mat_vect
        self.cost = self.calculate_cost(mat_vect, self.cost_vect)

    def __str__(self):
        return f"{self.name}, {self.cost}"

    @staticmethod
    def calculate_cost(mat, cost_vect):
        return np.dot(cost_vect, mat)


class Thruster:
    def __init__(self, name, grid, mass, thrust, fuel_rate, integrity, volume, t_area, t_volume, fuel_type):
        self.name = name
        self.grid = grid
        self.mass = mass
        self.thrust = thrust
        self.fuelRate = fuel_rate
        self.integrity = integrity
        self.volume = volume
        self.tArea = t_area
        self.tVolume = t_volume
        self.fuelType = fuel_type
        self.cost = 0

    def __str__(self):
        if self.grid == "Small":
            prefix = "s"
        else:
            prefix = "l"
        return f"{prefix}{self.name}: Relative Cost = {self.cost}"

    def set_cost(self, cost):
        self.cost = cost
