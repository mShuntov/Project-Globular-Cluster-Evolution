import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import os  
import glob
        
#Big Array

# Loop to read all the input files
filepath = "./M*.dat"
dat = glob.glob(filepath)
print('dat', dat)
for file in dat:
  #f = open(datafile, 'r') #Maybe you need a os.joinpath here, see Uku Loskit's answer, I don't have a python interpreter at hand
    print('datafile', file)
    #
    # with luminosities, temperatures and ages
    table = np.genfromtxt(file, dtype=None, unpack=True) 
    print('table.shape',table.shape)
    N_data = table.shape[1]
    #print('N_data = ', N_data)
    #print(table)
    #
    # Read luminositites from column #0
    lum = table[0, :]
    temp = table[1, :]
    age = table[2, :]

    #print('data', lum, temp, age)

    f = interp1d(age, temp)
    f2 = interp1d(age, temp, kind='cubic')

    agenew = np.linspace(3e6, 4e6, num=41, endpoint=True)
    #print('agenew', agenew)
    plt.plot(age, temp, 'o', agenew, f(agenew), '-', agenew, f2(agenew), '--')

plt.xscale('log')
plt.legend(['data', 'linear', 'cubic'], loc='best')
plt.show()