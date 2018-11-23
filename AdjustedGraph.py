import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



Server_Jan = pd.read_csv('Server_Jan.csv', usecols=[0])
J1 = Server_Jan.values

Server_Apr = pd.read_csv('Server_Apr.csv', usecols=[0])
A1 = Server_Apr.values

Server_Jul = pd.read_csv('Server_Jul.csv', usecols=[0])
S1 = Server_Jul.values

Elec = 50

SJ1 = J1 - Elec
SA1 = A1 - Elec
SS1 = S1 - Elec

Jan_Gas = pd.read_csv('Jan_Gas.csv', usecols=[0])
J2 = Jan_Gas.values

Apr_Gas = pd.read_csv('Apr_Gas.csv', usecols=[0])
A2 = Apr_Gas.values

Jul_Gas = pd.read_csv('Jul_Gas.csv', usecols=[0])
S2 = Jul_Gas.values

scaling = 7000/16000

SJ2 = scaling*J2
SA2 = scaling*A2
SS2 = scaling*S2


SJ3 = SJ1 + SJ2
SA3 = SA1 + SA2
SS3 = SS1 + SS2

plt.title('Adjusted Gas Load of OMPI Buiding')
plt.ylabel('kW0.5h')
plt.xlabel('Time')

plt.plot(SJ3, label='Jan Load')
plt.plot(SA3, label='Apr Load')
plt.plot(SS3, label='Jul Load')
plt.grid(axis='y')
plt.legend()

plt.show(block=True)