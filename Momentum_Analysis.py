#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Particle import Particle


# load the data file to be analysed.
Data = np.load("nBodyTest.npy", allow_pickle=True)


t = [] # create a list of time values to append to which is the x-axis
Niter = len(Data) # the number of iterations simulated is the length of the data
Nbody = len(Data[0]) - 1 # need to count the number of bodies to loop over but minus 1 as the first data row is time

Mom_tot = [] # list of total momenta for each time iteration


# prepare figure to be plotted
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 
ax.set_xlabel('Time /s')
ax.set_ylabel('Fractional Momentum') # fractional values don't have units


for i in range(0, Niter):
    
    t.append(Data[i][0]) # to take down all the time values at each time step
    
    Mom_time = np.zeros(3) # the momentum at a general time should reset back to a 3x1 0 vector NumPy array after each time iteration
    
    for j in range(0, Nbody):

        Mom_time += Data[i][j+1].Mom # loop through all the bodies and sum all their momenta together
        
    Mom_time_abs = np.linalg.norm(Mom_time) # the magnitude of the momentum needs to be plotted, can't plot the vector form
    
    Mom_tot.append(Mom_time_abs) # ceate a list of the magnitude of the momentum at each time iteration

frac_Mom = np.abs((Mom_tot-Mom_tot[0])/Mom_tot[0]) # fractional momentum change equation


ax.plot(t, frac_Mom, label = 'Fractional Momentum')
ax.legend(loc = 'upper left') # can change legends location
plt.savefig('SolarSystemPlotVerletMomentum.pdf')
plt.show()
