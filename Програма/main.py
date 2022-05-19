# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:02 2022

@author: romas
"""

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

epochs_threshold = 100

u = 1 # краще різні для обох алгоритмів


# оновлюються протягом роботи

learning_algorithm = 1 # можливо замість чистого алгоритму, використати їх комбінацію? Спочатку запустити генетичний, а потім зворотного поширення

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


res, err, epochs = c.learning_process(error_threshold, epochs_threshold, set_data, set_res, neurons, neuron_layer_quantity, eta, u, learning_algorithm)

i = 0

while i < len(res):

    j = 0

    while j < len(res[i]):

        res[i][j] = round(res[i][j], 3)

        j += 1

    i += 1

# print(f"Очікуваний вихід: {set_res}")

print(f"Отриманий результат: {res}")

print(f"Похибка: {err[-1]}")

print(f"Кількість епох навчання: {epochs}")

print()


# як будувати графік?

test_length = set_length

test_set_data = set_data.copy()

test_set_res = set_res.copy()


plt.figure(1)

i = 0

while i < len(res):

    plt.scatter(set_data[i][0], set_res[i], c = "red")

    plt.scatter(set_data[i][0], res[i], c = "blue")

    i += 1

plt.show()


plt.figure(2)

i = 0

x = []

y = []

while i < len(err):

    x.append(i)

    y.append(err[i])

    # plt.scatter(i, err[i], c = "blue")

    i += 1

plt.plot(x, y)

plt.show()
