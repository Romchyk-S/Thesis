# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import create_network as cn

import calculations as c

import get_data as gd

import learning_algorithms as la


# неоновлювані протягом роботи параметри

set_length = 1 # неправильно обчислює, якщо більше за 1, ваги нейронів стають більші за 1. Може, шукати через загальну похибку мережі?

eta = 0.005

entered_parms = 5

out_parms = 1

error = 10

error_threshold = 0.1


# оновлюються протягом роботи

learning_algorithm = 0

neurons_created = 0

neurons = []


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

while error > error_threshold:

    result = []

    i = 0

    while i < tr_length:

        result.append(c.calculate_result(neurons, tr_set_data[i]))

        i += 1

    error = c.calculate_error(neurons, tr_length, tr_set_data, tr_set_res, result)

    print(f"Загальна похибка мережі: {error}")

    # подумати про збереження вихідних ваг для порівняння

    print(neurons[0][0].get_weights())

    if learning_algorithm == 0:

        la.backpropagation(neurons, set_res, result, eta)

    elif learning_algorithm == 1:

        la.genetic(neurons, set_res, result)

    print(neurons[0][0].get_weights())

    print()


test_length = set_length

test_set_data = set_data.copy()

test_set_res = set_res.copy()




