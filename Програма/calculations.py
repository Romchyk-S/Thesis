# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:14:05 2022

@author: romas
"""

def activation_func(x):
    
    return x

def calculate_result(neur_arr, in_arr):

    i = 0

    while i < len(neur_arr)-1:
       
        in_arr = calculate_layer(neur_arr, in_arr, i).copy()
        
        i += 1
    
    return in_arr

def calculate_layer(neur_arr, in_arr, layer):
    
        res = []
    
        j = 0
        
        while j < len(neur_arr[layer+1]):
            
            
            k = 0
            
            weight_arr = neur_arr[layer][j].get_weights()
            
            
            while k < len(weight_arr):
                
                if k == 0:
                
                    res.append(weight_arr[k] * in_arr[j] + neur_arr[layer][j].get_bias())
                    
                else:
                    
                    # print(res)
                    
                    # print(j)
                    
                    # print(res[j])
                    
                    res[j] += weight_arr[k] * in_arr[j] + neur_arr[layer][j].get_bias()
                    
                    # print(res[j])
                    
                    # print()
                
                k += 1
                
            j += 1
            
        return res