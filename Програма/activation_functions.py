# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:04:24 2022

@author: romas
"""

def Leaky(x):

    #Leaky ReLU

    if x < 0:

        return 0.01*x

    else:

        return x
