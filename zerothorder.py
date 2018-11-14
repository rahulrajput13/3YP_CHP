# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:25:52 2018

@author: Saad-Rana
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import Assets as AS
import EnergySystem as ES      
import Market as MK

Jan_data = pd.read_csv('Elec15.01.17.csv', usecols = [0])
Jan_data.head()

#January usage day
#Jan_data.plot()
#plt.show(block=True)

nBuildings = 1
dt = 60/60 # duration o f individual period (h)
load_site1 = AS.loadAsset(nBuildings)
load_profile = load_site1.getOutput(dt)
print(load_profile[:5])

plt.plot(load_profile, label='load')
#plt.show(block=True)

#create constant CHP profile at 250 KW
CHP_profile = np.zeros(47)
for x in range(0,47):
    CHP_profile[x] = 250




t = type(CHP_profile)
print(t, CHP_profile)

plt.plot(CHP_profile, label='CHP output')

dispatchj = CHP_profile - load_profile



plt.plot(dispatchj, label='dispatchable output')
plt.ylabel('kW0.5h')
plt.xlabel('Time')


plt.show(block=True)


