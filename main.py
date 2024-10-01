from blocks import Thruster
from blocks import Part
from plottingfunctions import *

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # generate thruster components
    thrusterData = pd.read_csv("data/thrusterData.csv")
    componentData = pd.read_csv("data/componentBOM.csv")
    bpData = pd.read_csv("data/bpBOM.csv")

    pd.set_option('display.max_columns', None)

    # Components
    parts = []
    partVect = []
    # print(componentData)
    for series_name, series in componentData.items():
        if series_name != 'Refined Material' and series_name != 'Currency Value':
            partList = series.to_list()
            # print(partList)
            part = Part(series_name, partList)
            parts.append(part)
            partVect.append(part.cost)
            # print(part)

    # small grid thrusters
    sgThrusterData = thrusterData[thrusterData['Grid Type'] == "Small"]
    sgBPData = bpData[bpData['Grid Type'] == "Small"]
    sgThrusters = []

    for index, row in sgThrusterData.iterrows():
        tName = row['Name']
        thruster = Thruster(row['Name'], row['Grid Type'], row['Mass [kg]'], row['Thrust [N]'],
                            row['Fuel Consumption [L/s]'], row['Integrity'], row['Volume'],
                            row['Thrust Surface'],
                            row['Thrust/Volume'], row['Fuel Type'])
        sgThrusters.append(thruster)
        # print(thruster)
        bp = sgBPData.loc[sgBPData['Name'] == tName]
        bp_bom = bp.drop(['Name', 'Grid Type'], axis=1)
        bpVect = bp_bom.values.flatten().tolist()
        # print(f"{tName}{bpVect}")
        thruster.set_cost(np.dot(bpVect, partVect))
        # print(thruster)
        # print(bp_bom)
    thrust_vs_mass(sgThrusters, 'Small Grid')
    thrust_vs_cost(sgThrusters, 'Small Grid')
    thrust2cost(sgThrusters, 'Small Grid')
    thrust2mass(sgThrusters, 'Small Grid')

    # large grid thrusters
    lgThrusterData = thrusterData[thrusterData['Grid Type'] == "Large"]
    lgBPData = bpData[bpData['Grid Type'] == "Large"]
    lgThrusters = []

    for index, row in lgThrusterData.iterrows():
        tName = row['Name']
        thruster = Thruster(row['Name'], row['Grid Type'], row['Mass [kg]'], row['Thrust [N]'],
                            row['Fuel Consumption [L/s]'], row['Integrity'], row['Volume'],
                            row['Thrust Surface'],
                            row['Thrust/Volume'], row['Fuel Type'])
        lgThrusters.append(thruster)
        bp = lgBPData.loc[lgBPData['Name'] == tName]
        bp_bom = bp.drop(['Name', 'Grid Type'], axis=1)
        bpVect = bp_bom.values.flatten().tolist()
        # print(f"{tName}{bpVect}")
        thruster.set_cost(np.dot(bpVect, partVect))
        # print(thruster)

    thrust_vs_mass(lgThrusters, 'Large Grid')
    thrust_vs_cost(lgThrusters, 'Large Grid')
    thrust2cost(lgThrusters, 'Large Grid')
    thrust2mass(lgThrusters, 'Large Grid')

    plt.show()
