import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

Jan_Gas = pd.read_csv('Jan_Gas.csv', usecols=[0])
J1 = Jan_Gas.values

Apr_Gas = pd.read_csv('Apr_Gas.csv', usecols=[0])
A1 = Apr_Gas.values

Jul_Gas = pd.read_csv('Jul_Gas.csv', usecols=[0])
S1 = Jul_Gas.values

scaling = 7000/16000

SJ1 = scaling*J1
SA1 = scaling*A1
SS1 = scaling*S1

plt.title('Scaled Gas Load of OMPI Buiding')
plt.ylabel('kW0.5h')
plt.xlabel('Time')

plt.plot(SJ1, label='Jan Load')
plt.plot(SA1, label='Apr Load')
plt.plot(SS1, label='Jul Load')
plt.grid(axis='y')
plt.legend()

plt.show(block=True)