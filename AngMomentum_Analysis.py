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

AngMom_tot = []# list of total angular momenta for each time iteration


# preparing figure to be plotted
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 
ax.set_xlabel('Time /s')
ax.set_ylabel('Fractional Angular Momentum') # fractional values don't have units, see equation


for i in range(0, Niter):
    
    t.append(Data[i][0]) # to take down all the time values at each time step
    
    AngMom_time = np.zeros(3) # the angular momentum at a general time should reset back to a 3x1 0 vector NumPy array after each time iteration
    
    for j in range(0, Nbody):

        AngMom_time += Data[i][j+1].AngMom # loop through all the bodies and sum all their momenta together
        
    AngMom_time_abs = np.linalg.norm(AngMom_time) # the magnitude of the angular momentum needs to be plotted, can't plot the vector form
    
    AngMom_tot.append(AngMom_time_abs) # ceate a list of the magnitude of the angular momentum at each time iteration

dAngMom = np.abs((AngMom_tot-AngMom_tot[0])/AngMom_tot[0]) # fractional angular momentum change equation


ax.plot(t, dAngMom, label = 'Fractional Angular Momentum')
ax.legend(loc = 'upper left') # legends location can be altered
plt.savefig('SolarSystemPlotVerletAngularMomentum.pdf')
plt.show()
