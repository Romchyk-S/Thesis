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

                curr_layer[i].set_exit_value(j, exit_value)

                curr_layer[i].update_S(exit_value)

                if i == 0:

                    res.insert(j, exit_value)

                else:

                    res[j] += exit_value

                j += 1

            j = 0

            while j < len(res):

                res[j] = next_layer[j].get_activation_function_value(res[j])

                j += 1

            i += 1

        return res

def calculate_result(neur_arr, in_arr, learning_algorithm):

    i = 0

    while i < len(neur_arr)-1:

        in_arr = calculate_layer(neur_arr[i], neur_arr[i+1], in_arr, learning_algorithm)

        i += 1

    return in_arr

def calculate_error(exp_res, res, learning_algorithm):

    i = 0

    err = 0

    err_arr = []

    while i < len(exp_res):

        diff = exp_res[i]-res[i]

        err += diff

        if learning_algorithm == 0:

            err_arr.append(diff)

        i += 1

    if learning_algorithm == 0:

        return err, err_arr

    else:

        return err

def calculating_cycle(set_data, set_res, neur_arr, learning_algorithm):

    result = calculate_result(neur_arr, set_data, learning_algorithm)

    if learning_algorithm == 0:

        error, error_arr = calculate_error(set_res, result, learning_algorithm)

        return result, error, error_arr

    else:

        error = calculate_error(set_res, result, learning_algorithm)

        return result, error

def learning_cycle(neur_arr, neur_layer_arr, set_data, set_res, eta, batch, delta_w, learning_algorithm, w_bottom, w_upper):

    result = []

    i = 0

    while i < len(set_data):

        err_for_backprop = []

        if learning_algorithm == 0:

            res, error_for_i, err_for_backprop = calculating_cycle(set_data[i], set_res[i], neur_arr, learning_algorithm)

        else:

            res, error_for_i = calculating_cycle(set_data[i], set_res[i], neur_arr, learning_algorithm)

        error_for_i = round(error_for_i, 3)

        result.append(res)

        if i == 0:

            error = error_for_i**2

        else:

            error += error_for_i**2

        if learning_algorithm == 0:

            delta_w = la.backpropagation(neur_arr, result, eta, err_for_backprop, batch, i, delta_w)

            for n in neur_arr:

                for m in n:

                    m.set_S(0)

        if (i+1)%batch == 0 and learning_algorithm == 1:

            neur_arr = la.genetic(neur_arr, neur_layer_arr, len(set_res), set_data, set_res, w_bottom, w_upper)

        i += 1

    error /= len(set_res)

    if learning_algorithm == 1:

        return neur_arr, result, error, delta_w

    return result, error, delta_w


def learning_process(error_threshold, epochs_threshold, set_data, set_res, neur_arr, neur_layer_arr, eta, batch, learning_algorithm, w_bottom, w_upper):

    error = 1

    err_arr = []

    delta_w = []

    count = 0

    for n in neur_arr:

        temp_arr = []

        for m in n:

            temp_arr.append(0)

        delta_w.append(temp_arr)

    del delta_w[-1]


    while error > error_threshold and count < epochs_threshold:

        if learning_algorithm == 0:

            result, error, delta_w = learning_cycle(neur_arr, neur_layer_arr, set_data, set_res, eta, batch, delta_w, learning_algorithm, w_bottom, w_upper)

        else:

            neur_arr, result, error, delta_w = learning_cycle(neur_arr, neur_layer_arr, set_data, set_res, eta, batch, delta_w, learning_algorithm, w_bottom, w_upper)


        err_arr.append(error)

        count += 1

    return result, err_arr, count

def calculate_test_set(neur_arr, set_data, set_res):

    result = []

    i = 0

    while i < len(set_data):

        res, error_for_i = calculating_cycle(set_data[i], set_res[i], neur_arr, 1)

        error_for_i = round(error_for_i, 3)

        result.append(res)

        if i == 0:

            error = error_for_i**2

        else:

            error += error_for_i**2

        i += 1

    error /= len(set_res)

    return result, error