'''
Created by Maximo Xavier DeLeon
'''
import numpy as np
import math
import pandas as pd


'''
in this ~space~ we will take into account

Particles (aka point charges) : position (mass, charge, velocity, and other properties can be managed by the particle objects).
Electric Field: The Electric field produced by point charges (soon to be induced fields from increasing magnetic flux).
Magnetic Field: The Magnetic field produced by basic wire loops, magnets, and fields that have been spawned in.
Gravitational Field: Graviattional field as a result of masses in the space. Honestly might not add this until later.

- Thinking of creating a space class as the generic framework
- Field spaces will be child classes that inherit the properties of the space class. This will allow for me to create focus on each field type
- Will create final class which will be FieldSpace. This will be a class that can deal with particle placement along side all the fields within a space.

'''
class Space:
    def __init__(self):
        self.particles = {} # store the particles in the space as a dictionary

    def add_particle(self,particle,position,velocity=np.array([0,0,0]),verbose=False):
        name_is_unique = False # the name is not unique
        while not name_is_unique: # loop until the name is unique
            if particle.info.name not in self.particles.keys(): # if the name is not in the dictionary keys
                name_is_unique = True # then the name is unique

                # this starement here might throw an error since I dont think im properly indexing the position vectors
                #  \/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
                if position not in self.particles.values(): # if the particle has a unique position vector
                    self.particles[particle.info.name]  =  pd.Series([particle,position,velocity],['object','position','velocity']) # nest a pandas series storing particle properties an data
                    particle.exists_in_space = True # this will make it so the particle cannot be renamed once placed in the simulation space. Should stop any accidental renaming and crashing
                    if verbose:
                        print(particle.info.name) # print the particle's name/ if the user wants the method call to be verbose
                    else: pass

                else:
                    print('Error, two particles cannot occupy the same position in space. Particle', particle.info.name ,'not added!') # tell the user the position vector is not unique and their particle was not added
            else:
                old_name = particle.info.name # save the old name
                particle.rename(name=None) # if the particle's name is not unique then generate a new one for it
                print('The particle being addded to the space has a conflicting name so it has been given a new name.','OLD:', old_name,'NEW:',particle.info.name) # tell the user what the particle name/id was changed to

    # method for removing particles from the space
    def remove_particle(self,particle_id,verbose=False):
        if particle_id in self.particles.keys(): # if the particle name/id passed into the method exists in the dictionary storing the positions, then proceed
            if verbose: # if verbose then print stuff out
                print('Removing',particle_id,'from point', self.particles[particle_id]['position']) # tell the suer what is going to be deleted
                del self.particles[particle_id] # delete the entry
                print('Done.') # tell the user the deed has been done
            else: del self.particles[particle_id] # non verbose deletion of particle
        else: print('Error:', particle_id,'not found!') # if the particle id is not in the space dict then tell the user the particle was no found

    # method for listing particles present in the space
    def list_particles(self,verbose=True):
        data = [] # create an array to store particle data
        for key in self.particles: # iterate through all the values in the particle space dict
            value = self.particles[key] # simplify the indexing for the next few lines
            data.append({'id':key, # index particle name
                         'position':value['position'], # index the particle position vector
                         'velocity':value['velocity'], # index the particle velocity vector
                         'type':value['object'].particle_type, # index the particle type to the user
                         'mass':value['object']['mass'], # index the particle mass
                         'charge':value['object']['charge']}) # index the net charge of the particle

        particle_df = pd.DataFrame(data) # create a dataframe from the nested dictionary list
        if verbose: # print stuff out for the user if verbose
            print(particle_df)
        else: pass
        return particle_df # return the dataframe

    # save the configuration of the space including the position and properties of all particles
    def save_space(self,filename='R3_space.json',verbose=True):
        if verbose: # print stuff out for the user if verbose
            print('Saved particle space data as JSON file with the name', filename)
        else: pass
        self.list_particles(verbose=False).to_json(filename)  # save the dataframe as a JSON file



class ElectricFieldSpace(Space):
    def __init__(self):
        pass

    def calculate_strength(self):
        pass

class MagneticFieldSpace(Space):
    def __init__(self):
        pass