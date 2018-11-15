import numpy as np
import matplotlib.pyplot as plt
import pandas as pd




April_data = pd.read_csv('Elec15.04.17.csv', usecols=[0])
A1 = April_data.values

plt.plot(April_data)
CHP_profile = np.zeros(len(April_data))
for x in range(0,len(April_data)):
    CHP_profile[x] = 250

dispatch = CHP_profile - A1

plt.plot(dispatch)
plt.plot(CHP_profile)
plt.ylabel('kW0.5h')
plt.xlabel('Time')
plt.show(block=True)