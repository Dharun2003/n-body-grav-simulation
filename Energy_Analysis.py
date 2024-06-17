#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from Particle import Particle


# load the data file to be analysed.
Data = np.load("nBodyTest.npy", allow_pickle=True)


Niter = len(Data) # the number of iterations simulated is the length of the data
Nbody = len(Data[0]) - 1 # need to count the number of bodies to loop over but minus 1 as the first data row is time
t =[] # create a list of time values to append to which is the x-axis
# creating the list of total kinetic and potential energies to be added together to give total energy
KE_total = []
PE_total = []
E_tot = []
frac_E = []


# preparing the figure to be plotted
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1) 
ax.set_xlabel('Time /s')
ax.set_ylabel('Fractional Energy') # fractional values don't have units


for i in range(0, Niter):
    
    KE_tot = 0 # initialise and reset energy values for each time iteration
    PE_tot = 0
    
    t.append(Data[i][0]) # to take down all the time values at each time step
    
    for j in range(0, Nbody): # calcuatling the total KE and PE of the whole system for each time step
        
        KE_tot += Data[i][j+1].KE
        PE_tot += Data[i][j+1].PE
        
    KE_total.append(KE_tot) # one time step total KE/PE has been found so add to a list of total KE/PEs to be added together
    PE_total.append(PE_tot) # should be the same length as t


E_tot = list(np.array(KE_total) + np.array(PE_total)) # sum together to find the total energy

initE = [E_tot[0]] * len(E_tot) # find the inital energy value to compare all the others to
#print(initE)
   
frac_E = list(abs((np.array(E_tot) - np.array(initE)) / np.array(initE))) # equation for fractional energy change
     
             
ax.plot(t, frac_E, label = "Fractional Energy")

ax.legend(loc = 'upper right') # can change legend location
plt.savefig('SolarSystemPlotVerletEnergy.pdf')
plt.show()
