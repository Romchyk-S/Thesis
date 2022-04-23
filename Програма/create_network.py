# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 15:12:43 2022

@author: romas
"""

import neuron_class as nc


def get_layer_num(parms_in, parms_out):
    
    neur_layer_arr = []
    
    layer_num = int(input("Введіть кількість прихованих рівнів нейронної мережі: "))


    if layer_num > 0:

        i = 0
        
        while i < layer_num:
            
            neur_layer_arr.append(int(input(f"Введіть кількість нейронів на прихованому рівні {i}: ")))
            
            i += 1
            
        neur_layer_arr.insert(0, parms_in)
        
        neur_layer_arr.insert(len(neur_layer_arr), parms_out)
            
        print()
            
        print(f"Кількість рівнів: {layer_num+2}")
        
        print(f"Кількість нейронів на рівнях: {neur_layer_arr}")
        
    else:
        
        print(f"Кількість рівнів: {layer_num+2}")
        

    print()
        
    
    return layer_num, neur_layer_arr

def create_layer(num, quant, layer):
    
    # print(num)
    
    i = 0
    
    arr = []
    
    while i < num:
        
        arr.append(nc.Neuron(quant+i, layer))
        
        i += 1
    
    return arr

def add_weights(neur_arr, neur_layer_arr):
    
    for i in neur_arr:
        
        for j in i:
            
            try:
            
                j.add_weights(neur_layer_arr[j.get_layer()])
                
            except IndexError:
                
                break
            
def create_neurons(parms_in, parms_out, layer_num, neur_layer_arr):
    
    neurons_created = 0
    
    neur_arr = []
    
    i = 0
    
    while i < layer_num+2:
        
        if i == 0:
                
            neur_arr.append(create_layer(parms_in, neurons_created+1, i+1))
            
            neurons_created += parms_in
                
        elif i == layer_num+1:
            
            neur_arr.append(create_layer(parms_out, neurons_created+1, i+1))
            
            neurons_created += parms_out
            
        else:
                
            neur_arr.append(create_layer(neur_layer_arr[i], neurons_created+1, i+1))
            
            neurons_created += neur_layer_arr[i]
            
        i += 1  
        

    add_weights(neur_arr, neur_layer_arr)
    
    return neur_arr