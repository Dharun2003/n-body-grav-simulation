# -*- coding: utf-8 -*-
import numpy as np
class Particle:
    
    
    def __init__( # initialising all the values that are going to be used
        self,
        Bodies=[],
        position=np.array([0, 0, 0], dtype=float),
        velocity=np.array([0, 0, 0], dtype=float),
        acceleration=np.array([0, -10, 0], dtype=float),
        name='Ball',
        mass=1.0,
        G = 6.67408e-11,
        KE = 0,
        PE = 0,
        Mom = np.array([0, 0, 0], dtype=float),
        AngMom = np.array([0, 0, 0], dtype=float),
    ):
        self.mass = mass
        self.name = name
        self.G = G
        self.KE = KE
        self.PE = PE
        self.Mom = Mom
        self.AngMom = AngMom
        
        self.position = np.array(position, dtype = float)
        self.velocity = np.array(velocity, dtype = float)
        self.acceleration = np.array(acceleration, dtype = float)
        
    
    
    def __str__(self): # represent the class objects as strings to make the code more readable and easier to debug
        return "Particle: {0}, Mass: {1:.3e}, Position: {2}, Velocity: {3}, Acceleration: {4}".format(
            self.name, self.mass,self.position, self.velocity, self.acceleration
    )
    
    
    
    def updateGravitationalAcceleration(self, Bodies):
        """
        Returns the updated acceleration of the body as a 1x3 vector NumPy array.

        Parameters
        ----------
        Bodies : list of all the bodies in the system.
        
        Raises
        ------
        ValueError
            the mass of an object must be positive and this code checks that this is indeed the case to avoid any typos in the input data.

        Returns
        -------
        None.

        """
        if self.mass < 0:
            raise ValueError("The mass of the body {0} cannot be negative.".format(self.name))
            
        self.acceleration = np.array([0, 0, 0], dtype = float) # reset acceleration back to 0 for each new body
        
        for body in Bodies:
            if self.name != body.name: # avoids a divide by 0 error
                
                r = self.position - body.position
                dist = np.linalg.norm(r) # want to preserve the directional information of r and thus need r hat which can be written as r/dist
                
                self.acceleration += (- self.G * body.mass * r) / (dist ** 3)
                
            else:
                continue # so code continues when the loop passes over the same body
    
    
    
    def update(self, deltaT, Bodies, my_method):
        """
        This method uses the numerical approximation chosen by the user to calculate
        and update the position and velocities of the bodies in the system and
        calculates them as 1x3 vector NumPy arrays.

        Parameters
        ----------
        deltaT : the time step interval.
        Bodies : the list of all the objects in the system.
        my_method : the desired numerical method to be used.

        Raises
        ------
        TypeError
            raises an error if an incorrect method is chosen and lets the user know.

        Returns
        -------
        None.

        """
        if my_method == 'Euler':
            self.position = self.position + deltaT * self.velocity
            self.velocity = self.velocity + deltaT * self.acceleration
            
        elif my_method == 'Euler_Cromer':
            self.velocity = self.velocity + deltaT * self.acceleration
            self.position = self.position + deltaT * self.velocity
            
        elif my_method == 'Verlet':
            old_acceleration = self.acceleration
            self.position = self.position + self.velocity * deltaT + 1/2 * self.acceleration * deltaT ** 2
            self.updateGravitationalAcceleration(Bodies)
            self.velocity = self.velocity + 1/2 * (old_acceleration + self.acceleration) * deltaT
            
        else:
            raise TypeError("You have not chosen a valid numerical iteration method.")
                 
       
        
    def kineticEnergy(self):
        """
        Calculates the kinetic energy (scalar value) of the body.

        Returns
        -------
        None.

        """
        velocity_norm = np.linalg.norm(self.velocity) # convert velocity into speed as a scalar needs to be used to find  KE
        self.KE = 1/2 * self.mass * (velocity_norm ** 2)
        
    
    
    def potentialEnergy(self, Bodies):
        """
        Calculates the potential energy (scalar value) of the body.

        Returns
        -------
        None.

        """
        for body in Bodies:
            if self.name != body.name: # avoids a divide by 0 error, can't take PE w/ respect to itself
                r = np.linalg.norm(self.position - body.position) # need scalar distance to be used to calculate PE
                self.PE = - (self.G * self.mass * body.mass) / (2 * r ) # divide by 2 as each PE ends up being counted twice
        
    
    
    def Momentum(self):
        """
        Calculates the momentum (1x3 vector NumPy array) of the body.

        Returns
        -------
        None.

        """
        self.Mom = self.mass * self.velocity
        
    
    
    def AngMomentum(self):
        """
        Calculates the angular momentum (1x3 vector NumPy array) of the body.

        Returns
        -------
        None.

        """
        self.AngMom = np.cross(self.position, self.mass * self.velocity)
    
