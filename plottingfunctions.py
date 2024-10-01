import matplotlib.pyplot as plt
import numpy as np


def thrust_vs_mass(dfdata, title):
    fig, ax = plt.subplots()
    for dat in dfdata:
        ax.scatter(dat.thrust, dat.mass, label=dat.name)

    ax.legend(loc="lower right")
    plt.title(title + ' Thrust to Mass')
    plt.xlabel('Thrust [N]')
    plt.ylabel('Mass [kg]')


def thrust2mass(listdata, title):
    fig, ax = plt.subplots()
    y_pos = np.arange(len(listdata))
    names = []
    ratios = []
    for dat in listdata:
        ratio = dat.thrust / dat.mass
        names.append(dat.name)
        ratios.append(ratio)

    ax.barh(y_pos, ratios)
    ax.set_yticks(y_pos, labels=names)
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
