#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Particle import Particle


# load the data file to be analysed.
Data = np.load("nBodyTest.npy", allow_pickle=True)


Niter = len(Data) # the number of iterations simulated is the length of the data
"""Bodies = [] #need to recreate the Bodies list"""

# begin what the plot figure should look like
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 
ax.set_xlabel('Position in x-axis /m')
ax.set_ylabel('Poistion in y-axis /m')

    
"""for i in range(1, len(Data[-1])): # recreating Bodies list from data
    Bodies.append(Data[-1][i])"""

for i in range(1, len(Data[-1])): # defines set of axes for each body in Bodies
    x_axes = []
    y_axes = []

    for j in range(0, len(Data)): # create list of x and y positions for each body to plot
        x_axes.append(Data[j][i].position[0])
        y_axes.append(Data[j][i].position[1])

    ax.plot(x_axes, y_axes, label = Data[j][i].name) # plotting for each body and giving it the corresponding label


ax.legend(loc = 'lower left') # can alter where the legend appears
plt.savefig('SolarSystemPlotVerlet.pdf') # save as a pdf file to be used in the report
plt.show()


