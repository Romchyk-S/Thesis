# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:14:05 2022

@author: romas
"""

def activation_func(x):
    
    #Leaky ReLU
    
    if x < 0:
    
        return 0.01*x
    
    else:
        
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
                
                    res.append(activation_func(weight_arr[k] * in_arr[j] + neur_arr[layer][j].get_bias()))
                    
                else:
 
                    res[j] += weight_arr[k] * in_arr[j] + neur_arr[layer][j].get_bias()
                
                k += 1
                
            j += 1
            
        return res
    
def calculate_error(neur, length, data, exp_res):
    
    i = 0

    err = 0

    while i < length:

        res = calculate_result(neur, data[i])
        
        j = 0
        
        while j < len(res):
            
            err += (exp_res[i][j]-res[j])**2
            
            j += 1
        
        i += 1

    err *= 1/2
    
    return err