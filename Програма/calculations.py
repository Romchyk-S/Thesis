# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:14:05 2022

@author: romas
"""

import learning_algorithms as la


def calculate_layer(curr_layer, next_layer, in_arr, learning_algorithm):

        res = []

        i = 0

        while i < len(curr_layer):

            j = 0

            weight_arr = curr_layer[i].get_weights()

            while j < len(weight_arr):

                exit_value = weight_arr[j] * in_arr[i] + curr_layer[i].get_bias()

                # print("curr_layer")

                # print(curr_layer[i])

                # print(j)

                # print(exit_value)

                curr_layer[i].set_exit_value(j, exit_value)

                # print(curr_layer[i].get_exit_value(j))

                # print()

                if i == 0:

                    res.append(exit_value)

                else:

                    res[j] += exit_value

                j += 1

            if learning_algorithm == 0:

                j = 0

                while j < len(res):

                    next_layer[j].set_S(res[j])

                    next_layer[j].set_der_value_for_backprop(next_layer[j].get_S())

                    res[j] = next_layer[j].get_activation_function_value(res[j])

                    j += 1

            # print()

            i += 1

        return res

def calculate_result(neur_arr, in_arr, learning_algorithm):

    i = 0

    while i < len(neur_arr)-1:

        in_arr = calculate_layer(neur_arr[i], neur_arr[i+1], in_arr, learning_algorithm)

        i += 1

    for n in neur_arr:

        for m in n:

            m.set_S(0)

    return in_arr

def calculate_error(exp_res, res):

    i = 0

    err = 0

    while i < len(exp_res):

        err += exp_res[i]-res[i]

        i += 1

    return err

def calculating_cycle(set_data, set_res, neur_arr, learning_algorithm):

    result = calculate_result(neur_arr, set_data, learning_algorithm)

    error = calculate_error(set_res, result)

    return result, error

def learning_process(error_threshold, epochs_threshold, set_data, set_res, neur_arr, neur_layer_arr, eta, batch, learning_algorithm):

    error = 1

    err_for_backprop = 0

    count = 0

    err_arr = []

    while error > error_threshold and count < epochs_threshold:

        result = []

        i = 0

        while i < len(set_data):

            res, error_for_i = calculating_cycle(set_data[i], set_res[i], neur_arr, learning_algorithm)

            error_for_i = round(error_for_i, 3)

            result.append(res)

            if i == 0:

                error = error_for_i**2

                err_for_backprop = error_for_i

            else:

                error += error_for_i**2

                err_for_backprop += error_for_i

            if (i+1)%batch == 0:

                # print(i+1)

                if learning_algorithm == 0:

                    la.backpropagation(neur_arr, result, eta, err_for_backprop)

                    # if (i == 0 or i == 1) and (count == 0 or count == 1):

                    #     print(i)

                    #     print("weights")

                    #     for n in neur_arr:

                    #         for m in n:

                    #             print(m.get_weights())

                    #             print()


                # чи мають обнулитися err_for_i та err?

            i += 1


        error /= len(set_res)

        err_arr.append(error)

        if learning_algorithm == 1:

            neur_arr = la.genetic(neur_arr, neur_layer_arr, len(set_res), set_data, set_res)


        count += 1


    for n in neur_arr:

        for m in n:

            print(m.get_weights())

    return result, err_arr, count