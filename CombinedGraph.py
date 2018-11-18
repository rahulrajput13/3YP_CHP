import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

April_data = pd.read_csv('Elec15.04.17.csv', usecols=[0])
A1 = April_data.values

CHP_profile = np.zeros(len(April_data))
for x in range(0,len(April_data)):
    CHP_profile[x] = 250


dispatcha = CHP_profile - A1

Jan_data = pd.read_csv('Elec15.01.17.csv', usecols = [0])
J1 = Jan_data.values

dispatchj = CHP_profile - J1

July_data = pd.read_csv('Elec14.07.17.csv', usecols=[0])
S1 = July_data.values

dispatchs = CHP_profile - S1

plt.subplot(211)

plt.title('Electricity Load of OMPI Buiding')
plt.ylabel('kW0.5h')
plt.xlabel('Time')

plt.plot(CHP_profile,label='CHP Output')
plt.plot(J1, label='Jan Load')
plt.plot(April_data, label='Apr Load')
plt.plot(July_data, label='Jul Load')

plt.legend()


plt.subplot(212)

plt.title('Dispatchable Asset')
plt.ylabel('kW0.5h')
plt.xlabel('Time')

plt.plot(dispatchj, label='Jan Excess')
plt.plot(dispatcha, label='Apr Excess')
plt.plot(dispatchs, label='Jul Excess')

plt.legend()





plt.show(block=True)