'''
Created by Maximo Xavier DeLeon
'''


import numpy as np
import pandas as pd
import random
import string


ELEMENTARY_CHARGE = 1.60217662e-19 # coulombs

# particle parent class
class Particle:
    def __init__(self,mass, charge,name=None,particle_type=None):
        self.mass = mass # set the particle mass -- kg
        self.charge = charge # set the charge -- use coulombs
        # if no name has been given to the charge then gernerate a random name
        letters = string.ascii_letters
        self.particle_type = particle_type
        self.name = name if name is not None else str(particle_type) + '_' + str(''.join(random.choice(letters) for i in range(10)))
        self.exists_in_space = False # if this is set to true then renaming will be disabled
        '''if type(position) is list and len(position) == 3:
            self.position = np.array([[position[0]],
                                      [position[1]],
                                      [position[2]]])
        elif type(position) is np.ndarray and position.ndim == 1:
            self.position =position
        else:
            self.position = None

        self.velocity = velocity # velocity of the particle being spawned'''

        self.info = pd.Series([self.mass,self.charge],['mass','charge'],name=self.name) # return basic info about particle

    def rename(self,name=None):
        has_new_name = False
        while not has_new_name and not self.exists_in_space:

            if name is not self.name and not type(None):
                self.name = str(self.particle_type) + '_' + name
                has_new_name = True
            else:
                letters = string.ascii_letters
                rand_name = name if name is not None else str(''.join(random.choice(letters) for i in range(10)))
                if self.name[:10] is not rand_name:
                    self.name = str(self.particle_type) + '_' + rand_name
                    has_new_name = True
            self.info.name = self.name #= pd.Series([self.mass, self.charge], ['mass', 'charge'],name=self.name)  # return basic info about particle


# electron class inheriting particle properties
class Electron (Particle):
    def __init__(self,name=None):
        electron_mass = 9.11e-31 # kg
        electron_charge = -1*ELEMENTARY_CHARGE # coulombs
        Particle.__init__(self, electron_mass, electron_charge,name=name,particle_type='ELECTRON')

# proton class inheriting particle properties
class Proton (Particle):
    def __init__(self,name=None):
        proton_mass = 1.67e-27 # kg
        proton_charge = ELEMENTARY_CHARGE # coulombs
        Particle.__init__(self, proton_mass, proton_charge,name=name,particle_type='PROTON')

# neutron class inheriting particle properties
class Neutron (Particle):
    def __init__(self,name=None):
        neutron_mass = 9.11e-31 # kg
        neutron_charge = 0 # coulombs
        Particle.__init__(self, neutron_mass, neutron_charge,name=name,particle_type='NEUTRON')

# Atom class inheriting particle properties
class Atom (Particle):
    def __init__(self,symbol='H',name=None):
        self.reset(symbol) # will create the 'ideal' atom of the given symbol
        self.build(name) # initialize the particle with parent class features

    def reset(self,symbol): # reset parameters
        df = pd.read_csv('../PeriodicTable.csv')
        df.index = df['Symbol']
        self.summary = df.loc[symbol]
        self.neutrons = int(self.summary['NumberofNeutrons'])  # number of self.neutrons
        self.protons = int(self.summary['NumberofProtons'])  # number of self.protons
        self.electrons = int(self.summary['NumberofElectrons'])  # number of self.electrons


    def build(self,name=None): # establish the parameters with parent class
        self.mass = (1.67e-27 * self.neutrons) + (1.67e-27 * self.protons) + (9.11e-31 * self.electrons)  # kg
        self.net_charge = (ELEMENTARY_CHARGE * self.protons) + (-1 * ELEMENTARY_CHARGE * self.electrons)  # coulombs
        Particle.__init__(self, self.mass, self.net_charge,name=name,particle_type='ATOM')

    def ionize(self, electron_change): # option to ionize the particle
        self.electrons = self.electrons + electron_change
        self.build()
