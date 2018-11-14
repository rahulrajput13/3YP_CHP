# -*- coding: utf-8 -*-

"""
3YP main setup file.
Adapted from UoO EPG's energy management framework.
Authors: Avinash Vijay, Scot Wheeler
"""

__version__ = '0.2'

#import modules

import numpy as np
import matplotlib.pyplot as plt
import Assets as AS
import EnergySystem as ES      
import Market as MK
        
#######################################
### STEP 1: setup parameters
#######################################

dt = 30/60 # 30 minute time intervals
T = int(24/dt) #Number of intervals

#######################################
### STEP 2: setup the assets 
#######################################

dispatchable = []
non_dispatchable = []
all_assets = []

#PV source
pv_capacity = 3 # kW
pv_site1 = AS.pvAsset(pv_capacity)
non_dispatchable.append(pv_site1)

#Load
nHouses = 1
load_site1 = AS.loadAsset(nHouses)
non_dispatchable.append(load_site1)

#Battery
battery_capacity = 2.5 # kWh
battery_power = 1 # kW
battery_eff = 0.6
#battery_site1 = AS.IdealBatteryAsset(battery_capacity, battery_power, dt, T)
battery_site1 = AS.PracticalBatteryAsset(battery_capacity, battery_power,
                                     battery_eff, dt, T)
dispatchable.append(battery_site1)

#######################################
#STEP 4: setup and run the energy system
#######################################

# setup
energy_system = ES.EnergySystem(non_dispatchable, dispatchable, dt, T)
# run
net_load = energy_system.basic_energy_balance()

#######################################
### STEP 6: setup and run the market
#######################################

# setup
market1 = MK.marketObject()
# run
opCost = market1.getOpCost(net_load)
print('Operating cost: £ %3.3f'%(opCost/100))

# #######################################
# ### STEP 7: plot results
# #######################################

#plt.stackplot(np.array(range(48)), pv_site1.output, hydro_site1.output)
labels = ['PV Output', 'Battery Operation']
ax = plt.subplot(1,1,1)
p1 = plt.stackplot(np.arange(48), pv_site1.output.T, battery_site1.output.T, labels=labels)
p2 = plt.plot(load_site1.output, '-k', label='Load')
plt.xticks([0,12,24,36,48])
ax.set_xticklabels(['00:00','06:00','12:00','18:00','00:00'])
plt.ylabel('(kWh)', color='k')
plt.xlabel('Time', color='k')
ax.legend()
#plt.legend()
#plt.plot(battery_site1.soc/battery_site1.capacity)
plt.show()
#plt.pause(0.01)