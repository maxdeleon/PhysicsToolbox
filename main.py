import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import particle
import pandas as pd
import math

# quick main to test particle classes
# YES I KNOW SOME ELEMENTS EXIST AS DIATOMIC MOLECULES I WILL FIX THAT SOON


e_field = 10e4 # V/m

def e_field_acceleration(mass,charge,e_field):
    return (charge*e_field)/mass

def v_f(a,t):
    return a*t
def d_x(a,t):
    return 0.5*a*t**2



total_time = 1
time_step = 0.000001
time_table = np.arange(total_time/time_step)

elements = ['C','Y','Ni','Cu']

element_df = pd.read_csv('PeriodicTable.csv')
symbols = element_df.Symbol


element_dict ={}
velocities = {}

for element in elements:
    element_dict[element] = particle.Atom(element,None)
    element_dict[element].ionize(-1)

    acceleration = e_field_acceleration(element_dict[element].mass,
                                        element_dict[element].charge,
                                        e_field)
    #velocities[element] = v_f(acceleration,time_table)
    velocities[element] = d_x(acceleration,time_table) # this is actually calculating position. very quick fix


df = pd.DataFrame.from_dict(velocities)
print(df)

df.plot()
plt.show()


