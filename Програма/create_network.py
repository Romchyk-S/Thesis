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

    print()

    neur_layer_arr.insert(0, parms_in)

    neur_layer_arr.insert(len(neur_layer_arr), parms_out)

    print(f"Кількість рівнів: {layer_num+2}")

    print(f"Кількість нейронів на рівнях: {neur_layer_arr}")

    print()

    return layer_num, neur_layer_arr

def create_layer(num, quant, layer, func, func_der, bias_bottom, bias_upper):

    i = 0

    arr = []

    while i < num:

        arr.append(nc.Neuron(quant+i, layer, func, func_der, bias_bottom, bias_upper))

        i += 1

    return arr

def add_weights(neur_arr, neur_layer_arr, *args):

    i = 0

    while i < len(neur_arr)-1:

        for j in neur_arr[i]:

            try:

                if len(args) == 2:

                    j.add_random_weights(neur_layer_arr[j.get_layer()], args[0], args[1])

                else:

                    j.add_weights_from_arr(args[0][j.get_index()-1])


            except IndexError:

                print("IndErrS")

                print()

                break

        i += 1

def create_neurons(parms_in, parms_out, layer_num, neur_layer_arr, func_arr, func_der_arr, *args):

    neurons_created = 0

    neur_arr = []

    # потрібен ефективніший спосіб

    # ELU: 0
    # Leaky: 1
    # Linear: 2
    # ReLU: 3
    # ReLU6: 4
    # SELU: 5
    # Sigmoid: 6
    # Softplus: 7
    # Tanh: 8

    activ_func_index_in = 0

    activ_func_index_hidden = 6

    activ_func_index_out = 0

    i = 0

    while i < layer_num+2:

        if i == 0:

            neur_arr.append(create_layer(parms_in, neurons_created+1, i+1, func_arr[activ_func_index_in], func_der_arr[activ_func_index_in], args[0], args[1]))

            neurons_created += parms_in

        elif i == layer_num+1:

            neur_arr.append(create_layer(parms_out, neurons_created+1, i+1, func_arr[activ_func_index_out], func_der_arr[activ_func_index_out], args[0], args[1]))

            neurons_created += parms_out

        else:

            neur_arr.append(create_layer(neur_layer_arr[i], neurons_created+1, i+1, func_arr[activ_func_index_hidden], func_der_arr[activ_func_index_hidden], args[0], args[1]))

            neurons_created += neur_layer_arr[i]

        i += 1

    if len(args) > 0:

        if len(args) == 2:

            add_weights(neur_arr, neur_layer_arr, args[0], args[1])

        else:

            add_weights(neur_arr, neur_layer_arr, args[0])

            # так само треба для зміщення

    return neur_arr
