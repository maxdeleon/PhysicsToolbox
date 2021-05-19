import numpy as np
import pandas as pd

ELEMENTARY_CHARGE = 1.60217662e-19 # coulombs

# particle parent class
class Particle:
    def __init__(self,mass, charge, position=None):
        self.mass = mass # set the particle mass -- kg
        self.charge = charge # set the charge -- use coulombs

        if type(position) is list and len(position) == 3:
            self.position = np.array([[position[0]],
                                      [position[1]],
                                      [position[2]]])
        elif type(position) is np.ndarray and position.ndim == 1:
            self.position =position
        else:
            self.position = None

    def move(self, delta_vector): # method enables user to move the particle via addition of the position vectors
        if type(delta_vector) is np.ndarray:
            self.position = self.position + delta_vector
        else:
            print("Particle not moved. Ensure that the delta vector is in numpy array format.")

    def place(self, position_vector): # set the particle's position given a position vector
        if type(position_vector) is np.ndarray:
            self.position = position_vector
        else:
            print("Particle position not set. Ensure that the delta vector is in numpy array format.")

# electron class inheriting particle properties
class Electron (Particle):
    def __init__(self,position=None):
        electron_mass = 9.11e-31 # kg
        electron_charge = -1*ELEMENTARY_CHARGE # coulombs
        Particle.__init__(self, electron_mass, electron_charge,position)

# proton class inheriting particle properties
class Proton (Particle):
    def __init__(self, position=None):
        proton_mass = 1.67e-27 # kg
        proton_charge = ELEMENTARY_CHARGE # coulombs
        Particle.__init__(self, proton_mass, proton_charge, position)

# neutron class inheriting particle properties
class Neutron (Particle):
    def __init__(self, position=None):
        neutron_mass = 9.11e-31 # kg
        neutron_charge = 0 # coulombs
        Particle.__init__(self, neutron_mass, neutron_charge, position)

# Atom class inheriting particle properties
class Atom (Particle):
    def __init__(self,symbol='H',position=None):
        self.reset(symbol) # will create the 'ideal' atom of the given symbol
        self.position = position # define the position
        self.build() # initialize the particle with parent class features

    def reset(self,symbol): # reset parameters
        df = pd.read_csv('PeriodicTable.csv')
        df.index = df['Symbol']
        self.summary = df.loc[symbol]
        self.neutrons = int(self.summary['NumberofNeutrons'])  # number of self.neutrons
        self.protons = int(self.summary['NumberofProtons'])  # number of self.protons
        self.electrons = int(self.summary['NumberofElectrons'])  # number of self.electrons


    def build(self): # establish the parameters with parent class
        self.mass = (1.67e-27 * self.neutrons) + (1.67e-27 * self.protons) + (9.11e-31 * self.electrons)  # kg
        self.net_charge = (ELEMENTARY_CHARGE * self.protons) + (-1 * ELEMENTARY_CHARGE * self.electrons)  # coulombs
        Particle.__init__(self, self.mass, self.net_charge, self.position)

    def ionize(self, electron_change): # option to ionize the particle
        self.electrons = self.electrons + electron_change
        self.build()
