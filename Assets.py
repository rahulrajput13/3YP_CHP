#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3YP basic asset module.
Adapted from UoO EPG's energy management framework.
Authors: Avinash Vijay, Scot Wheeler
"""

__version__ = '0.2'

import pandas as pd
import numpy as np

class Non_Dispatchable:
    """Non-dispatchable asset base class"""
    def __init__(self):
        self.dispatch_type = "Non-dispatchable"
        
class Dispatchable:
    """Dispatchable asset base class"""
    def __init__(self):
        self.dispatch_type = "Dispatchable"

#%% Non-dispatchable assets

class pvAsset(Non_Dispatchable):
    """
    PV asset class
    
    Input
    -----
    Capacity : float
        PV capacity, kW.
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.asset_type = 'PV'
        super().__init__()
        
    def getOutput(self, dt):
        """
        Return PV output
        
        Input
        -----
        dt : float
            Time interval (hours)
            
        Returns
        -------
        PV output : numpy array
        """
        df = pd.read_csv('data/solar02Jan.csv', usecols=[0])
        solar = df.values
        output = solar * self.capacity * dt
        self.output = output
        return output
    
class loadAsset(Non_Dispatchable):
    """
    Load asset class
    
    Input
    -----
    nHouses : int
        Number of houses
    """
    def __init__(self, nBuildings):
        self.nBuildings = nBuildings
        self.asset_type = 'DOMESTIC_LOAD'
        super().__init__()
    
    def getOutput(self, dt):
        """
        Return domestic demand
        
        Input
        -----
        dt : float
            Time interval (hours)
            
        Returns
        -------
        Domestic demand : numpy array
        """
        df = pd.read_csv('Elec15.01.17.csv', usecols=[0])
        dem = df.values
        output = dem * self.nBuildings * dt
        self.output = output
        return output
    
#%% Dispatchable Assets
    
class IdealBatteryAsset(Dispatchable):
    """
    Ideal battery asset class
    
    Input
    -----
    Capacity : float
        Battery capacity, kWh.
    
    power : float
        Maximum power, kW.
        
    dt : float
        Time interval (hours)
            
    T : int
        Number of intervales
    """
    def __init__(self, capacity, power, dt, T):
        self.capacity = capacity
        self.power = power * dt
        self.soc = np.ones(T) * self.capacity
        super().__init__()
        
    def getOutput(self, net_load):
        """
        Battery control of charging/discharging in response to net load.
        
        Input
        -----
        net_load : numpy array
            The net load, (load - nondispatchable gen).
            
        Returns
        -------
        Battery energy use profile : numpy array
        """
        T = len(net_load)
        output = np.zeros(T)
        for j in range(len(net_load)):
            if j == 0:
                soc = self.capacity
            else:
                soc = self.soc[j-1]
                
            if net_load[j] > 0: # use battery
                output[j] = min(self.power, net_load[j], soc)
                self.soc[j] = soc - output[j]
            elif net_load[j] < 0: # charge battery
                output[j] = max(-self.power, net_load[j],
                      -(self.capacity - soc))
                self.soc[j] = soc - output[j]
            elif net_load[j] == 0: # do nothing
                self.soc[j] = soc
        self.output = output
        return output
    
class PracticalBatteryAsset(Dispatchable):
    """
    Practical battery asset class
    
    Input
    -----
    Capacity : float
        Battery capacity, kWh.
    
    power : float
        Maximum power, kW.
        
    eff : float
        Charging/discharging efficiency between 0-1.
        
    dt : float
        Time interval (hours)
            
    T : int
        Number of intervales
    """
    def __init__(self, capacity, power, eff, dt, T):
        self.capacity = capacity
        self.power = power * dt
        self.eff = eff
        self.soc = np.ones(T) * self.capacity
        super().__init__()
        
    def getOutput(self, net_load):
        """
        Battery control of charging/discharging in response to net load.
        
        Input
        -----
        net_load : numpy array
            The net load, (load - nondispatchable gen).
            
        Returns
        -------
        Battery energy use profile : numpy array
        """
        
        T = len(net_load)
        output = np.zeros(T)
        for j in range(len(net_load)):
            if j == 0:
                soc = self.capacity
            else:
                soc = self.soc[j-1]
                
            if net_load[j] > 0: # use battery
                output[j] = min(self.power, net_load[j], self.eff*soc)
                self.soc[j] = soc - (1/self.eff)*output[j]
            elif net_load[j] < 0: # charge battery
                output[j] = max(-self.power, net_load[j],
                      -(1/self.eff)*(self.capacity - soc))
                self.soc[j] = soc - self.eff*output[j]
            elif net_loadl[j] == 0: # do nothing
                self.soc[j] = soc
        self.output = output
        return output