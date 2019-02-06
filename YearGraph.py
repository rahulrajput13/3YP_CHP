import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

OMPI = pd.read_csv('FormattedElec.csv')

x = range(0,8520)


plt.figure(1)
plt.plot(x,OMPI['usage'].values)
plt.title('Electricity Load thorughout Year')
plt.xlabel('Time')
plt.ylabel('KWh')
plt.show()