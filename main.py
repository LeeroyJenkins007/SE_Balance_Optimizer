from blocks import Thruster, costVect
from blocks import costVect
from plottingfunctions import *
from components import MaterialCost

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

RELOAD = True


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
        # print(componentData)
        bpData = pd.read_pickle("data/bpData.pkl")
        fuel_pumpData = pd.read_pickle("data/fuel_pumpData.pkl")

    pd.set_option('display.max_columns', None)

    ## Time to run data specific calculations based on type of data
    # Components
    # calculate the relative cost for the
    componentCost = []
    for index, row in componentData.iterrows():
        # print(row)
        componentCost.append(row.drop(['Name']).dot(costVect))
        # print(cost)
    componentData['Cost'] = componentCost

    # thrusters
    t2m = [] # thrust to mass
    tCost = []
    t2c = [] # thrust to cost
    t2a = [] # thrust to area
    for index, dat in thrusterData.iterrows():
        # add thrust 2 mass ratio
        t2m.append(dat['Thrust [N]'] / dat['Mass [kg]'])
        # add cost and thrust 2 cost ratio
        bp = bpData[(bpData['Name'] == dat['Name']) & (bpData['Grid Type'] == dat['Grid Type'])]
        bp_bom = bp.drop(['Name', 'Grid Type'], axis=1)
        bpVect = bp_bom.values.flatten().tolist()
        cost = np.dot(bpVect, componentCost)
        tCost.append(cost)
        t2c.append(dat['Thrust [N]'] / cost)

    thrusterData['Thrust/Mass'] = t2m
    thrusterData['Cost'] = tCost
    thrusterData['Thrust/Cost'] = t2c


    # Sample plots
    # thrust2cost(thrusterData[thrusterData['Grid Type'] == 'Small'], 'Small Grid Test')
    # thrust2mass(thrusterData[thrusterData['Grid Type'] == 'Small'], 'Small Grid Test')

    thrust_vs_cost(thrusterData[thrusterData['Grid Type'] == 'Large'], 'Large Grid')
    thrust_vs_mass(thrusterData[thrusterData['Grid Type'] == 'Large'], 'Large Grid')
    thrust2cost(thrusterData[thrusterData['Grid Type'] == 'Large'], 'Large Grid')
    thrust2mass(thrusterData[thrusterData['Grid Type'] == 'Large'], 'Large Grid')

    plt.show()
