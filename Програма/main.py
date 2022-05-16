# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import create_network as cn

import get_data as gd

import learning_algorithms as la


print()


# неоновлювані протягом роботи параметри

set_length = 200

eta = 0.005

entered_parms = 5

out_parms = 1

error_threshold = 0.1

batch_length = 5


# оновлюються протягом роботи

learning_algorithm = 0 # можливо замість чистого алгоритму, використати їх комбінацію? Спочатку запустити генетичний, а потім зворотного поширення

neurons_created = 0

neurons = []


set_data, set_res = gd.get_dataset(set_length, entered_parms)


print("Вхід:")

print(set_data)

print("Вихід:")

print(set_res)

print()


# є проблеми, якщо відсутні проміжні рівні

layer_number, neuron_layer_quantity = cn.get_layer_num(entered_parms, out_parms)

neurons = cn.create_neurons(entered_parms, out_parms, layer_number, neuron_layer_quantity)

print(neurons)

print()


# розділяти на tr_set і test_set

tr_length = set_length

tr_set_data = set_data.copy()

tr_set_res = set_res.copy()



if learning_algorithm == 0:

    res, err, epochs = la.backpropagation_calculation(error_threshold, tr_set_data, tr_set_res, neurons, eta, batch_length)

    i = 0

    while i < len(res):

        j = 0

        while j < len(res[i]):

            res[i][j] = round(res[i][j], 3)

            j += 1

        i += 1

    print(f"Отриманий результат: {res}")

    print(f"Вихід: {set_res}")

    print(f"Похибка: {err}")

    print(f"Кількість епох навчання: {epochs}")

    print()

elif learning_algorithm == 1:

    la.genetic(neurons,  neuron_layer_quantity, tr_length, tr_set_data, tr_set_res, error_threshold)


# як будувати графік?

test_length = set_length

test_set_data = set_data.copy()

test_set_res = set_res.copy()




