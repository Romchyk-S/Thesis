# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import create_network as cn

import get_data as gd

import calculations as calc

import copy as c


print()


# Notice that because deltas are accumulated over all training items, the order in which training data
# is processed doesn't matter, as opposed to online training where it's critically important to visit items
# IN A RANDOM ORDER.


# неоновлювані протягом роботи параметри

error_threshold = 0.01

epochs_threshold = 200

weight_bottom = -1

weight_upper = 1

# для зворотного поширення помилки

eta = 0.005

# для генетичного алгоритму

crossover_prob = 0.75

mutation_prob = 0.45

population_length = 10

ga_weight_bottom = -1

ga_weight_upper = 1

# оновлюються протягом роботи

neurons_created = 0

neurons = []


set_data, set_res = gd.get_dataset("data")

set_data = gd.normalise(set_data)

set_res = gd.normalise(set_res)


in_parms = len(set_data[0])

out_parms = len(set_res[0])


tr_set_data = set_data[::2]

tr_set_res = set_res[::2]

test_set_data = set_data[1::2]

test_set_res = set_res[1::2]

activ_funcs, activ_funcs_ders = gd.get_activation_funcs()


layer_number, neuron_layer_quantity = cn.get_layer_num(in_parms, out_parms)

neurons = cn.create_neurons(in_parms, out_parms, layer_number, neuron_layer_quantity, activ_funcs, activ_funcs_ders, weight_bottom, weight_upper)

neurons_1 = c.deepcopy(neurons)

# для потенційного комбінованого алгоритму
# neurons_2 = c.deepcopy(neurons)


# зворотне поширення помилки

u = 1

calc.main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neurons, neuron_layer_quantity, eta, u, 0)


# генетичний

u = len(tr_set_data)

calc.main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neurons_1, neuron_layer_quantity, eta, u, 1, ga_weight_bottom, ga_weight_upper, activ_funcs, activ_funcs_ders, crossover_prob, mutation_prob, population_length)


# подумати про комбінований алгоритм: спочатку знайти локальний оптимум генетичним (можливо, з іншим значенням epochs_threshold). Потім наблизитися до глобального за допомогою зворотного поширення
# потрібно правильно визначати номери фігур