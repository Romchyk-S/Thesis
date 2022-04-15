# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import create_network as cn

import calculations as c


learning_algorithm = 0

neurons = []

entered_parms = 5

out_parms = 1

neurons_created = 0

D = [10, 20, 10, 11, 15]

R = [12]



layer_number, neuron_layer_quantity = cn.get_layer_num(entered_parms, out_parms)

neurons = cn.create_neurons(entered_parms, out_parms, layer_number,  neuron_layer_quantity)

print(neurons)

print()



res = c.calculate_result(neurons, D)

print(res)