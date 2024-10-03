import matplotlib.pyplot as plt
import numpy as np


# function to add value labels
def addhorzlabels(x,y):
    for i in range(len(x)):
        plt.text(x[i], y[i], str(round(x[i])), ha = 'center', va = 'center')


def thrust_vs_mass(dfdata, title):
    fig, ax = plt.subplots()
    for dat in dfdata:
        ax.scatter(dat.thrust, dat.mass, label=dat.name)

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
    for dat in dfdata:
        ax.scatter(dat.thrust, dat.cost, label=dat.name)

    ax.legend(loc="lower right")
    plt.title(title + ' Thrust to Cost')
    plt.xlabel('Thrust [N]')
    plt.ylabel('Cost [-]')


def thrust2cost(listdata, title):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(listdata))
    names = []
    ratios = []
    for dat in listdata:
        ratio = dat.thrust / dat.cost
        names.append(dat.name)
        ratios.append(ratio)

    ax.barh(y_pos, ratios)
    ax.set_yticks(y_pos, labels=names)
    ax.set_title(f'Thrust to Cost Ratios: {title}')


def thrust2costV2(thrusterData, title):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(thrusterData))
    names = []
    ratios = []
    for dat in thrusterData:
        print(dat)
        ratio = dat['Thrust [N]'] / dat['Cost']
        names.append(dat['Name'])
        ratios.append(ratio)

    ax.barh(y_pos, ratios)
    ax.set_yticks(y_pos, labels=names)
    ax.set_title(f'Thrust to Cost Ratios: {title}')