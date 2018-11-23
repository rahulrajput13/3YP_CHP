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

plt.title('Server Room Cooling load')
plt.ylabel('kW0.5h')
plt.xlabel('Time')

plt.plot(SJ1, label='Jan Load')
plt.plot(SA1, label='Apr Load')
plt.plot(SS1, label='Jul Load')
plt.grid(axis='y')
plt.legend()

plt.show(block=True)