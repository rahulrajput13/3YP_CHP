import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import Assets as AS
import EnergySystem as ES      
import Market as MK


July_data = pd.read_csv('Elec14.07.17.csv', usecols=[0])
A1 = July_data.values

plt.plot(July_data)
CHP_profile = np.zeros(len(July_data))
for x in range(0,len(July_data)):
    CHP_profile[x] = 250

dispatch = CHP_profile - A1

plt.plot(dispatch)
plt.plot(CHP_profile)
plt.ylabel('kW0.5h')
plt.xlabel('Time')
plt.show(block=True)