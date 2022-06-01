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

in_parms = 2

out_parms = 1

error_threshold = 0.01

epochs_threshold = 200

weight_bottom = -1

weight_upper = 1

# для зворотного поширення помилки

eta = 0.005

# для генетичного алгоритму

crossover_prob = 0.85

mutation_prob = 0.25

population_length = 10

# оновлюються протягом роботи

neurons_created = 0

neurons = []



activ_funcs, activ_funcs_ders = gd.get_activation_funcs()


tr_set_data, tr_set_res, test_set_data, test_set_res = gd.get_dataset(in_parms)


layer_number, neuron_layer_quantity = cn.get_layer_num(in_parms, out_parms)

neurons = cn.create_neurons(in_parms, out_parms, layer_number, neuron_layer_quantity, activ_funcs, activ_funcs_ders, weight_bottom, weight_upper)

neurons_1 = c.deepcopy(neurons)

neurons_2 = c.deepcopy(neurons)



# розібратися з nan, коли багато лінійних функцій
# мабуть, необхідно буде проводити нормалізацію на кожному рівні

u = 1

calc.main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neurons, neuron_layer_quantity, eta, u, 0)


u = len(tr_set_data)

calc.main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neurons_1, neuron_layer_quantity, eta, u, 1, weight_bottom, weight_upper, activ_funcs, activ_funcs_ders, crossover_prob, mutation_prob, population_length)





# подумати про комбінований алгоритм: спочатку знайти локальний оптимум генетичним (можливо, з іншим значенням epochs_threshold). Потім наблизитися до глобального за допомогою зворотного поширення
# потрібно правильно визначати номери фігур