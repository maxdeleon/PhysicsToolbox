import math
import numpy as np
import pandas as pd

ELECTRIC_PERMITTIVITY_OF_FREE_SPACE = 8.85e-12 #F/m
MAGNETIC_PERMITTIVITY_OF_FREE_SPACE = math.pi*4e-7 #H/m

def lorentz_force(q,E,v,B):
    # Method to calculate the lorentz force on a charge in either an electric field, magnetic field, or both
    return q*(E + np.cross(v,B)) # returns a numpy vector

def uniform_ppc_e_field(voltage,distance, area_vector):
    '''
    Method to calculate the uniform electric field between the plates of a parallel plate capacitor

    :param voltage:
    electrical potential difference between the two plates

    :param distance:
    distance between the two plates

    :param area_vector:
    vector perpendicular to the surface of anode and pointing towards the cathode
    :return:

    return a electric field vector
    '''
    return (voltage/distance) * area_vector.norm()

def uniform_solenoid_b_field(turns,length,current, area_vector):
    '''
    :param turns:
    turns of wire in solenoid
    :param length:
    length of solenoid
    :param current:
    current passinf through solenoid wire
    :param area_vector:
    direction of thumb in right hand rule (direction of north end of solenoid)
    :return:
    '''
    return MAGNETIC_PERMITTIVITY_OF_FREE_SPACE*current*(turns/length) * area_vector.norm()






























