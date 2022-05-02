# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import create_network as cn

import calculations as c

import get_data as gd


learning_algorithm = 0

eta = 0.005

neurons = []

entered_parms = 5

out_parms = 1

neurons_created = 0




set_length = 10

set_data, set_res = gd.get_dataset(set_length, entered_parms)

# розділяти на tr_set і test_set

print(set_data)

print(set_res)

print()


layer_number, neuron_layer_quantity = cn.get_layer_num(entered_parms, out_parms)

neurons = cn.create_neurons(entered_parms, out_parms, layer_number, neuron_layer_quantity)

print(neurons)

print()


tr_length = set_length

tr_set_data = set_data.copy()

tr_set_res = set_res.copy()

result = []

i = 0

while i < tr_length:

    result.append(c.calculate_result(neurons, tr_set_data[i]))

    i += 1

error = c.calculate_error(neurons, tr_length, tr_set_data, tr_set_res, result)

print(f"Загальна похибка мережі: {error}")


# тут запускати алгоритми навчання


test_length = set_length

test_set_data = set_data.copy()

test_set_res = set_res.copy()




