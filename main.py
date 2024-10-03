from blocks import Thruster
from blocks import Part
from plottingfunctions import *
from components import MaterialCost

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

RELOAD = False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # run when changes to any of the .csv's
    if RELOAD:
        # generate thruster components
        thrusterData = pd.read_csv("data/source/thrusterData.csv")
        thrusterData.to_pickle("data/thrusterData.pkl")

        componentData = pd.read_csv("data/source/componentBOM.csv")
        componentData.to_pickle("data/componentData.pkl")

        bpData = pd.read_csv("data/source/bpBOM.csv")
        bpData.to_pickle("data/bpData.pkl")

        fuel_pumpData = pd.read_csv("data/source/fuelpumpData.csv")
        fuel_pumpData.to_pickle("data/fuel_pumpData.pkl")
    else:
        thrusterData = pd.read_pickle("data/thrusterData.pkl")
        componentData = pd.read_pickle("data/componentData.pkl")
        print(componentData)
        bpData = pd.read_pickle("data/bpData.pkl")
        fuel_pumpData = pd.read_pickle("data/fuel_pumpData.pkl")

    pd.set_option('display.max_columns', None)

    ## Time to run data specific calculations based on type of data
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
    # costVect = cost_func()

    # thrusters
    t2m = [] # thrust to mass
    t2c = [] # thrust to cost
    t2a = [] # thrust to area
    for index, dat in thrusterData.iterrows():
        t2m.append(dat['Thrust [N]'] / dat['Mass [kg]'])
        # add cost and thrust 2 cost ratio

    thrusterData['Thrust/Mass'] = t2m
    # print(thrusterData)

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
    # thrust_vs_mass(sgThrusters, 'Small Grid')
    # thrust_vs_cost(sgThrusters, 'Small Grid')
    # thrust2cost(sgThrusters, 'Small Grid')
    # thrust2costV2(thrusterData[thrusterData['Grid Type'] == 'Small Grid'], 'Small Grid Test')
    thrust2mass(thrusterData[thrusterData['Grid Type'] == 'Small'], 'Small Grid Test')

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

    # thrust_vs_mass(lgThrusters, 'Large Grid')
    # thrust_vs_cost(lgThrusters, 'Large Grid')
    # thrust2cost(lgThrusters, 'Large Grid')
    thrust2mass(thrusterData[thrusterData['Grid Type'] == 'Large'], 'Large Grid')

    plt.show()
