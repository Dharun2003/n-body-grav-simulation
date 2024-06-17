#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from Particle import Particle
import copy


# using the following format below, the user can add up to as many bodies as 
# they wish by inputting the appropriate data in the same format.
# the data used here was taken from the JPL website.
# don't forget to add the new body name to the Bodies list below!

earth_EMB_Mass = 5.97237e24
earth_EMB_Radius = 6371 * 1e3  
Earth_EMB = Particle(
    position = np.array([3.3725e6, -3.5626e6, -4.4301e5]),
    velocity = np.array([8.4388e0, 8.1808e0, 3.2620e-2]),
    acceleration = np.array([0, 0, 0]),
    name = "Earth_EMB",
    mass = earth_EMB_Mass
)
moon_EMB_Mass = 7.349e22
moon_EMB_Radius = 1738 * 1e3  
Moon_EMB = Particle(
    position = np.array([-2.7419e8, 2.8964e8, 3.6017e7]),
    velocity = np.array([-6.8608e2, -6.6511e2, -2.6521e0]),
    acceleration = np.array([0, 0, 0]),
    name = "Moon_EMB",
    mass = moon_EMB_Mass
)
sunMass = 1988500e24
sunRadius = 695700 * 1e3
Sun = Particle(
    position = np.array([-1.3570e9, 3.9841e7, 3.1283e7]),
    velocity = np.array([1.2023e0, -1.5641e1, 1.0165e-1]),
    acceleration = np.array([0, 0, 0]),
    name = "Sun",
    mass = sunMass
)
mercuryMass = 3.302e23
mercuryRadius = 2440 * 1e3
Mercury = Particle(
    position = np.array([4.9126e10, -3.0367e10, 7.0840e9]),
    velocity = np.array([1.5576e4, 4.3944e4, 2.1639e3]),
    acceleration = np.array([0, 0, 0]),
    name = "Mercury",
    mass = mercuryMass
)
venusMass = 48.69e23
venusRadius = 6052 * 1e3
Venus = Particle(
    position = np.array([3.6670e10, -1.0192e11, -3.5644e9]),
    velocity = np.array([3.2575e4, 1.2112e4, -1.7130e3]),
    acceleration = np.array([0, 0, 0]),
    name = "Venus",
    mass = venusMass
)
earthMass = 5.97237e24
earthRadius = 6371 * 1e3  
Earth = Particle(
    position = np.array([2.2643e10, 1.4536e11, 2.3194e7]),
    velocity = np.array([-2.9865e4, 4.7330e3, 4.0959e-2]),
    acceleration = np.array([0, 0, 0]),
    name = "Earth",
    mass = earthMass
)
marsMass = 6.4171e23
marsRadius = 3396 * 1e3
Mars = Particle(
    position = np.array([4.5678e10, 2.2562e11, 3.6052e9]),
    velocity = np.array([-2.2800e4, 6.9900e3, 7.0623e2]),
    acceleration = np.array([0, 0, 0]),
    name = "Mars",
    mass = marsMass
)
jupiterMass = 189819e19
jupiterRadius = 69911 * 1e3
Jupiter = Particle(
    position = np.array([7.2690e11, 1.3434e11, -1.6820e10]),
    velocity = np.array([-2.5240e3, 1.3461e4, 5.9770e-01]),
    acceleration = np.array([0, 0, 0]),
    name = "Jupiter",
    mass = jupiterMass
)
saturnMass = 5.6834e26
saturnRadius = 58232 * 1e3
Saturn = Particle(
    position = np.array([1.2094e12, -8.3660e11, -3.3606e10]),
    velocity = np.array([4.9547e3, 7.9243e3, -3.3447e2]),
    acceleration = np.array([0, 0, 0]),
    name = "Saturn",
    mass = saturnMass
)
uranusMass = 86.813e24
uranusRadius = 25362 * 1e3
Uranus = Particle(
    position = np.array([2.0070e12, 2.1511e12, -1.8012e10]),
    velocity = np.array([-5.0294e3, 4.3284e3, 8.1375e1]),
    acceleration = np.array([0, 0, 0]),
    name = "Uranus",
    mass = uranusMass
)
neptuneMass = 102.409e24
neptuneRadius = 24624 * 1e3
Neptune = Particle(
    position = np.array([4.4500e12, -4.4916e11, -9.3305e10]),
    velocity = np.array([5.0956e2, 5.4400e3, -1.2361e2]),
    acceleration = np.array([0, 0, 0]),
    name = "Neptune",
    mass = neptuneMass
)


# the four following lines are the inputs that the user can change

deltaT = 24 * 60 * 60 # time step interval
Nt = int(120 * 365.25 * 24 * 60 * 60 / deltaT) # number of iterations to simulate 
Bodies = [Sun, Mercury, Venus, Earth, Mars, Jupiter] # Add the new body name to this list
my_method = 'Verlet' # chose a numerical approximation technique to use here



Data = [] # initialise the Data list to append all the calculated data to



for i in range(0, Nt+1):
    
    # calculate all the initial energies and momenta first and save it to the
    # data file before updating their acceleration, velocities, and positions
    
    for body in Bodies:
        body.kineticEnergy()
        
    for body in Bodies:
        body.potentialEnergy(Bodies)
        
    for body in Bodies:
        body.Momentum()
        
    for body in Bodies:
        body.AngMomentum()
    
    if i % 10 == 0: # saves data for every time step, this can be changed to make the program run faster
        data_list = [deltaT * i]
        for body in Bodies:
            data_list.append(copy.deepcopy(body))
        Data.append(data_list)
            
    for body in Bodies:
        body.updateGravitationalAcceleration(Bodies)
        
    for body in Bodies:
        body.update(deltaT, Bodies, my_method)

           
np.save("nBodyTest", Data, allow_pickle=True)   # saving the data file          
            
            
      