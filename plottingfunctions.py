import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# function to add value labels
def addhorzlabels(x, y, precision):
    for i in range(len(x)):
        plt.text(x[i], y[i], str(round(x[i], precision)), ha='center', va='center')


def thrust_vs_mass(dfdata, title):
    fig, ax = plt.subplots()
    for index, dat in dfdata.iterrows():
        ax.scatter(dat['Thrust [N]'], dat['Mass [kg]'], label=dat['Name'])

    ax.legend(loc="lower right")
    plt.title(title + ' Thrust to Mass')
    plt.xlabel('Thrust [N]')
    plt.ylabel('Mass [kg]')


def thrust2mass(thrusterData, title):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(thrusterData))
    names = []
    ratios = []
    for index, dat in thrusterData.iterrows():
        ratio = dat['Thrust [N]'] / dat['Mass [kg]']
        names.append(dat['Name'])
        ratios.append(ratio)

    ax.barh(y_pos, ratios)
    ax.set_yticks(y_pos, labels=names)
    addhorzlabels(ratios, y_pos)
    ax.set_title(f'Thrust to Mass Ratios: {title}')


def thrust_vs_cost(dfdata, title):
    fig, ax = plt.subplots()
    for index, dat in dfdata.iterrows():
        ax.scatter(dat['Thrust [N]'], dat['Cost'], label=dat['Name'])

    ax.legend(loc="lower right")
    plt.title(title + ' Thrust to Cost')
    plt.xlabel('Thrust [N]')
    plt.ylabel('Cost [-]')


def thrust2cost(thrusterData, title):
    # print(thrusterData)
    fig, ax = plt.subplots()
    y_pos = np.arange(len(thrusterData))
    names = []
    ratios = []
    for index, dat in thrusterData.iterrows():
        # print(dat)
        ratio = dat['Thrust [N]'] / dat['Cost']
        # print(ratio)
        names.append(index)
        ratios.append(ratio)

    ax.barh(y_pos, ratios)
    ax.set_yticks(y_pos, labels=names)
    ax.set_title(f'Thrust to Cost Ratios: {title}')


def thrust2fuel(thrusterData, fuelType, title):
    fig, ax = plt.subplots()
    names = []
    consume = []
    for index, dat in thrusterData[thrusterData['Fuel Type'] == fuelType].iterrows():
        # print(f'Is DataFrame: {isinstance(dat, pd.Series)}')
        #print(dat['Fuel Consumption'])
        names.append(index)
        consume.append(dat['Fuel Consumption'])

    y_pos = np.arange(len(names))

    ax.barh(y_pos, consume)
    ax.set_yticks(y_pos, labels=names)
    addhorzlabels(consume, y_pos, 2)
    ax.set_title(f'Fuel Consumption: {title}')


def thrust2base(thrusterData, baseName):
    # print(thrusterData)
    # print(f"{thrusterData.index = }")
    fig, ax = plt.subplots()
    #print(baseData)
    baseData = thrusterData.loc[baseName]
    # print(f'Is DataFrame: {isinstance(baseData, pd.DataFrame)}')
    # print(baseData)
    baseL = baseData['Length']
    # print(baseL)
    baseW = baseData['Width']
    baseT = baseData['Thrust [N]']
    # print(baseT)
    y_pos = np.arange(len(thrusterData))
    # print(y_pos)
    names = []
    ratios = []
    for index, dat in thrusterData.iterrows():
        #print(index)
        # tSurface = dat['Length'] * dat['Width']
        numBase = np.floor(dat['Length'] / baseL) * np.floor(dat['Width'] / baseW)
        theoreticalT = numBase * baseT
        # print()
        ratio = dat['Thrust [N]'] / theoreticalT
        # print(ratio)
        names.append(index)
        ratios.append(ratio)

    # print(ratios)
    ax.barh(y_pos, ratios)
    ax.set_yticks(y_pos, labels=names)
    addhorzlabels(ratios, y_pos, 2)
    ax.set_title(f'Thrust Relative to {baseName}, By Area Restriction')


def pltcost(thrusterData, title):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(thrusterData))
    names = []
    costs = []
    for index, dat in thrusterData.iterrows():
        # print(dat)
        #ratio = dat['Thrust [N]'] / dat['Cost']
        # print(ratio)
        names.append(index)
        costs.append(dat['Cost'])

    ax.barh(y_pos, costs)
    ax.set_yticks(y_pos, labels=names)
    addhorzlabels(costs, y_pos, 2)
    ax.set_title(f'Relative Cost: {title}')


def topContender(thrusterData, title):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(thrusterData))
    names = []
    costs = []
    costRanking = thrusterData.sort_values(by = 'Cost')
    masses = []
    thrusts = []
    fuelrates = []
    for index, dat in thrusterData.iterrows():

        names.append(index)
        costs.append(dat['Cost'])

    ax.barh(y_pos, costs)
    ax.set_yticks(y_pos, labels=names)
    addhorzlabels(costs, y_pos, 2)
    ax.set_title(f'Relative Cost: {title}')
