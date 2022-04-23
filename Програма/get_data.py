# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:13:44 2022

@author: romas
"""

import random as r

def get_dataset(length, entered_parms):
    
    data = []

    exp_res = []

    i = 0

    while i < length:

        D = []

        R = []

        j = 0
        
        while j < entered_parms:
            
            D.append(r.randint(1, 20))
            
            j += 1
        
        R.append(r.randint(1, 20))
        
        data.append(D)
        
        exp_res.append(R)
        
        i += 1
        
    return data, exp_res