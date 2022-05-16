# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:14:05 2022

@author: romas
"""


def calculating_cycle(set_data, set_res, neur_arr):

    result = (calculate_result(neur_arr, set_data))

    error = calculate_error(neur_arr, set_data, set_res, result)

    return result, error

def calculate_result(neur_arr, in_arr):

    i = 0

    while i < len(neur_arr)-1:

        in_arr = calculate_layer(neur_arr[i], neur_arr[i+1], in_arr)

        i += 1

    return in_arr

def calculate_layer(curr_layer, next_layer, in_arr):

        res = []

        i = 0

        while i < len(curr_layer):

            j = 0

            weight_arr = curr_layer[i].get_weights()


            while j < len(weight_arr):

                # print("weight")

                # print(weight_arr)

                exit_value = weight_arr[j] * in_arr[i] + curr_layer[i].get_bias()

                curr_layer[i].set_exit_value(j, exit_value)


                if i == 0:

                    res.append(exit_value)

                else:

                    res[j] += exit_value

                j += 1

            j = 0

            while j < len(res):

                # next_layer[j].set_S(next_layer[j].get_S()+round(res[j], 3))

                # print("res")

                # print(res)

                # print()

                next_layer[j].set_S(res[j])

                next_layer[j].set_der_value_for_backprop(next_layer[j].get_S())

                res[j] = next_layer[j].get_activation_function_value(res[j])

                j += 1

            # print()

            i += 1

        return res

def calculate_error(neur, data, exp_res, res):

    i = 0

    err = 0

    while i < len(exp_res):

        err += exp_res[i]-res[i]

        i += 1

    return err
