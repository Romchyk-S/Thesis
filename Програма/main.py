# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import inspect as insp

import activation_functions as af

import create_network as cn

import get_data as gd

import calculations as calc

import copy as c



print()


functions_list = insp.getmembers(af, insp.isfunction)

activ_funcs = []

activ_funcs_ders = []

i = 0

while i < len(functions_list):

    if i%2 == 0:

        activ_funcs.append(functions_list[i][1])

    else:

        activ_funcs_ders.append(functions_list[i][1])

    i += 1



# Notice that because deltas are accumulated over all training items, the order in which training data
# is processed doesn't matter, as opposed to online training where it's critically important to visit items
# IN A RANDOM ORDER.


# неоновлювані протягом роботи параметри

set_length = 200

eta = 0.005

entered_parms = 5

out_parms = 1

error_threshold = 0.01

epochs_threshold = 150

weight_bottom = -1

weight_upper = 1


neurons_created = 0

neurons = []


set_data, set_res = gd.get_dataset(set_length, entered_parms)

tr_set_data = set_data[::2]

tr_set_res = set_res[::2]

test_set_data = set_data[1::2]

test_set_res = set_res[1::2]


# є проблеми, якщо відсутні проміжні рівні

layer_number, neuron_layer_quantity = cn.get_layer_num(entered_parms, out_parms)

neurons = cn.create_neurons(entered_parms, out_parms, layer_number, neuron_layer_quantity, activ_funcs, activ_funcs_ders, weight_bottom, weight_upper)


neurons_1 = c.deepcopy(neurons)

neurons_2 = c.deepcopy(neurons)


print("Навчальна вибірка")

print("Вхід:")

print(tr_set_data)

print("Вихід:")

print(tr_set_res)

print()



u = 1

calc.main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neurons, neuron_layer_quantity, eta, u, 0)


u = len(tr_set_data)

calc.main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neurons_1, neuron_layer_quantity, eta, u, 1, weight_bottom, weight_upper, activ_funcs, activ_funcs_ders)



# подумати про комбінований алгоритм: спочатку знайти локальний оптимум генетичним (можливо, з іншим значенням epochs_threshold). Потім наблизитися до глобального за допомогою зворотного поширення
# потрібно правильно визначати номери фігур