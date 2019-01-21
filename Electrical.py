import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


OMPI = pd.read_csv('OMPI_Data.csv')
SWDP = pd.read_csv('SWDP_Data.csv')

x = np.arange(0,24,0.5)

plt.figure(1)
plt.plot(x,OMPI[['Elec1']], label='Fixed')
plt.plot(x,(OMPI[['Elec1']]+SWDP[['Elec1']]), label='Flexible')
plt.title('January Electricity Load')
plt.xlabel('Time')
plt.ylabel('KW0.5h')
plt.legend()
plt.show()

plt.figure(2)
plt.plot(x,OMPI[['Elec2']],label='Fixed')
plt.plot(x,(OMPI[['Elec2']]+SWDP[['Elec2']]),label='Flexible')
plt.title('April Electricity Load')
plt.xlabel('Time')
plt.ylabel('KW0.5h')
plt.legend()
plt.show()

plt.figure(3)
plt.plot(x,OMPI[['Elec3']],label='Fixed')
plt.plot(x,(OMPI[['Elec3']]+SWDP[['Elec3']]),label='Flexible')
plt.title('July Electricity Load')
plt.xlabel('Time')
plt.ylabel('KW0.5h')
plt.legend()
plt.show()