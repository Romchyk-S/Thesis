# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

import activation_functions as af

import create_network as cn

import get_data as gd

import calculations as c

import matplotlib.pyplot as plt


print()

# Notice that because deltas are accumulated over all training items, the order in which training data
# is processed doesn't matter, as opposed to online training where it's critically important to visit items
# IN A RANDOM ORDER.


# неоновлювані протягом роботи параметри

set_length = 200

eta = 0.005

entered_parms = 5

out_parms = 1

error_threshold = 0.01

epochs_threshold = 500

weight_bottom = -1

weight_upper = 1


# оновлюються протягом роботи

learning_algorithm = 1 # можливо замість чистого алгоритму, використати їх комбінацію? Спочатку запустити генетичний, а потім зворотного поширення

neurons_created = 0

neurons = []


set_data, set_res = gd.get_dataset(set_length, entered_parms)

tr_set_data = set_data[::2]

tr_set_res = set_res[::2]

test_set_data = set_data[1::2]

test_set_res = set_res[1::2]

u = len(tr_set_data)

u = 1


# є проблеми, якщо відсутні проміжні рівні

layer_number, neuron_layer_quantity = cn.get_layer_num(entered_parms, out_parms)

neurons = cn.create_neurons(entered_parms, out_parms, layer_number, neuron_layer_quantity, [weight_bottom, weight_upper])


print("Навчальна вибірка")

print("Вхід:")

print(tr_set_data)

print("Вихід:")

print(tr_set_res)

print()


tr_res, tr_err, epochs = c.learning_process(error_threshold, epochs_threshold, tr_set_data, tr_set_res, neurons, neuron_layer_quantity, eta, u, learning_algorithm, weight_bottom, weight_upper)

i = 0

while i < len(tr_res):

    j = 0

    while j < len(tr_res[i]):

        tr_res[i][j] = round(tr_res[i][j], 3)

        j += 1

    i += 1

print(f"Отриманий результат: {tr_res}")

print(f"Похибка: {tr_err[-1]}")

print(f"Кількість епох навчання: {epochs}")

print()



plt.figure(1)

plt.title(f"Навчальна вибірка, похибка {tr_err[-1]}")

i = 0

while i < len(tr_res):

    plt.scatter(tr_set_data[i][0], tr_set_res[i], c = "red")

    plt.scatter(tr_set_data[i][0], tr_res[i], c = "blue")

    i += 1

plt.show()


plt.figure(2)

plt.title("Крива навчання мережі")

i = 0

x = []

y = []

while i < len(tr_err):

    x.append(i)

    y.append(tr_err[i])

    # plt.scatter(i, tr_err[i])

    i += 1

plt.plot(x, y)

plt.show()


print("Тестова вибірка")

test_res, test_err = c.calculate_test_set(neurons, test_set_data, test_set_res)

i = 0

while i < len(test_res):

    j = 0

    while j < len(test_res[i]):

        test_res[i][j] = round(test_res[i][j], 3)

        j += 1

    i += 1


print(f"Отриманий результат: {test_res}")

print(f"Похибка: {test_err}")

print()


plt.figure(3)

plt.title(f"Тестова вибірка, похибка {test_err}")

i = 0

while i < len(test_res):

    plt.scatter(test_set_data[i][0], test_set_res[i], c = "red")

    plt.scatter(test_set_data[i][0], test_res[i], c = "blue")

    i += 1

plt.show()