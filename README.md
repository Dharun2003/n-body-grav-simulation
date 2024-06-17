# n-body-grav-simulation
# Phys 281 Project ReadMe File
@Dharun Venkat

## Simulation.py 
-> Simulation file where instances of the class Particle are created to form the n-nody system,
the bodies are then advanced according to the method chosen, and the results are saved to a data file. 
Requires NumPy and copy. Tested on Python 3.9.
This is the only script that the user should alter. The user can add extra bodies with their required data in the same format done 
for the bodies already there and the user can also change the time step interval, the number of iterations (how long the simulation 
runs for), and add/removes bodies from the Bodies list to change the bodies being simulated. Lastly, the user can chose the numerical 
approximation method used to run the simulation.

## Particle.py 
-> Particle class containing the methods required to update the gravitational acceleration, compute the new velocities and
positions of the bodies using the chosen numerical method and advance the system. It also calculated the energies, momenta, and angular 
momenta of the bodies.
Requires NumPy. Tested on Python 3.9.
Requires no user input.

## Orbit_Analysis.py 
-> Post-processing script to analyse the positions saved in the data file to plot the orbits of the bodies. 
Requires NumPy and matplotlib. Tested on Python 3.9.
The user can change the location of the legend if desired.

## Energy_Analysis.py 
-> Post-processing script to analyse the kinetic and potential energies saved in the data file to plot the 
fractional total energy change of the system over time. 
Requires NumPy and matplotlib. Tested on Python 3.9.
The user can change the location of the legend if desired.

##Momentum_Analysis.py 
-> Post-processing script to analyse the momenta saved in the data file to plot the total
fractional total momentum change of the system over time. 
Requires NumPy and matplotlib. Tested on Python 3.9.
The user can change the location of the legend if desired.

## AngMomentum_Analysis.py 
-> Post-processing script to analyse the angular momenta saved in the data file to plot the 
fractional total angular momentum change of the system over time. 
Requires NumPy and matplotlib. Tested on Python 3.9.
The user can change the location of the legend if desired.
