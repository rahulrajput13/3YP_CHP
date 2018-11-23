import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Server_Jan = pd.read_csv('Server_Jan.csv', usecols=[0])
J2 = Server_Jan.values

Server_Apr = pd.read_csv('Server_Apr.csv', usecols=[0])
A2 = Server_Apr.values

Server_Jul = pd.read_csv('Server_Jul.csv', usecols=[0])
S2 = Server_Jul.values

Elec = 50

CJ1 = J2 - Elec
CA1 = A2 - Elec
CS1 = S2 - Elec


Jan_data = pd.read_csv('Elec15.01.17.csv', usecols = [0])
J1 = Jan_data.values

Solar_Jan = pd.read_csv('SJan.csv', usecols=[0])
SJ1 = Solar_Jan.values

Load1 = J1 - SJ1 - CJ1

April_data = pd.read_csv('Elec15.04.17.csv', usecols=[0])
A1 = April_data.values

Solar_April = pd.read_csv('SApr.csv', usecols=[0])
SA1 = Solar_April.values

Load2 = A1 - SA1 - CA1

July_data = pd.read_csv('Elec14.07.17.csv', usecols=[0])
S1 = July_data.values

Solar_July = pd.read_csv('SJuly.csv', usecols=[0])
SS1 = Solar_July.values

Load3 = S1 - SS1 - CS1

CHP_profile = np.zeros(len(April_data))
for x in range(0,len(April_data)):
    CHP_profile[x] = 250


dispatchj = CHP_profile - J1
dispatcha = CHP_profile - A1
dispatchs = CHP_profile - S1

plt.title('Electricity Load of OMPI Buiding')
plt.ylabel('kW0.5h')
plt.xlabel('Time')

plt.plot(Load1, label='Jan Load')
plt.plot(Load2, label='Apr Load')
plt.plot(Load3, label='Jul Load')
plt.grid(axis='y')
plt.legend()


plt.show(block=True)