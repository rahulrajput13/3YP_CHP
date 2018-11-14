#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
3YP basic market module.
Authors: Avinash Vijay, Scot Wheeler
"""

import pandas as pd

class marketObject:
    """
    Market class for calculating energy price.
    """
    def __init__(self):
        data1 = pd.read_csv('data/mip.csv', header=None, usecols=[1,2,3,4])
        apxData = data1[data1[1].str.contains('APXMIDP')]
        self.mip = apxData[4].values / 10 # convert £/mWh to p/kWh
        
    def getOpCost(self, net_load):
        """
        Calculate total cost of net electricity.
        
        Input
        -----
        net_load : numpy array
        
        Returns
        -------
        Total cost (£)
        """
        cost = 0
        for i in range( len(net_load) ):
            cost += net_load[i] * self.mip[i]
        return cost
    