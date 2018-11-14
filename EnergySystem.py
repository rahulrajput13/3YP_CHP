#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3YP basic Energy System module.
Adapted from UoO EPG's energy management framework.
Authors: Avinash Vijay, Scot Wheeler
"""

__version__ = '0.2'

import numpy as np


class EnergySystem:
    """
    Base Energy System class
    
    Input
    -----
    nondispat : list
        List of non-dispatchable asset objects
    
    dispat : list
        List of dispatchable assets. The order of which determines control 
        strategy in basic energy balance.
        
    dt : float
        time step
    
    T : float
        Number of time intervals
    """
    
    def __init__(self, nondispat, dispat, dt, T):
        self.nondispat = nondispat
        self.dispat = dispat
        self.dt = dt #time interval duration
        self.T = T #number of time intervals
        
    def basic_energy_balance(self):
        """
        Basic energy system balancing. Dispatchable assets are deployed in
        order defined by list. 
        
        Returns
        -------
        
        net_load : Array
            The net load of the system.
        """
        nondispat = self.nondispat # nondispatcable asset list
        dispat = self.dispat # dispatchable asset list
        
        # sum non-dispatchable assets
        net_nondis = np.zeros(self.T) 
        for i, asset in enumerate(nondispat):
            if asset.asset_type == 'DOMESTIC_LOAD':
                profile = nondispat[i].getOutput(self.dt)
            elif asset.asset_type == 'PV': 
                profile = -1 * nondispat[i].getOutput(self.dt) # might want -1 inside asset
            
            for j in range(self.T):
                    net_nondis[j] += profile[j]
        
        net_load = net_nondis
        
        # deploy dispatchable gen
        for i, asset in enumerate(dispat):                
            surplus = net_load
            profile = asset.getOutput(surplus)
            net_load = surplus - profile
        
        return net_load