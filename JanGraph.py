# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 14:25:52 2018

@author: Saad-Rana
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


Jan_data = pd.read_csv('Elec15.01.17.csv', usecols = [0])
J1 = Jan_data.values

plt.plot(Jan_data)
CHP_profile = np.zeros(len(Jan_data))
for x in range(0,len(Jan_data)):
    CHP_profile[x] = 250

dispatch = CHP_profile - J1

plt.plot(dispatch)
plt.plot(CHP_profile)
plt.ylabel('kW0.5h')
plt.xlabel('Time')
plt.show(block=True)


