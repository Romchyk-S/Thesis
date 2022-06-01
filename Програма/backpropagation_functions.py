# -*- coding: utf-8 -*-
"""
Created on Fri May 20 12:36:03 2022

@author: romas
"""

def set_errors(neur_arr, err):

    i = len(neur_arr)-1

    while i >= 0:

        j = 0

        while j < len(neur_arr[i]):

            if i == len(neur_arr)-1:

                # neur_arr[i][j].set_error(err[j])

                neur_arr[i][j].set_error(err[j]*neur_arr[i][j].get_activation_function_der_value(neur_arr[i][j].get_S()))

            else:

                k = 0

                while k < len(neur_arr[i+1]):

                    neur_arr[i][j].set_error(neur_arr[i][j].get_weight(k)*neur_arr[i+1][k].get_error())

                    k += 1

            j += 1

        i -= 1

def update_delta_w(neur_arr, eta, delta_w_arr, delta_w_bias_arr, iteration, batch):

    i = len(neur_arr)-1

    while i > 0:

            j = 0

            while j < len(neur_arr[i]):

                k = 0

                while k < len(neur_arr[i-1]):

                    f_der = neur_arr[i-1][k].get_activation_function_der_value(neur_arr[i-1][k].get_S())

                    delta_w_temp = neur_arr[i-1][k].get_error()*f_der

                    delta_w = eta*delta_w_temp*neur_arr[i-1][k].get_exit_value(j)

                    delta_w_bias = eta*delta_w_temp

                    try:

                        delta_w_arr[i-1][k] += delta_w

                    except IndexError:

                        delta_w_arr[i-1].insert(k, delta_w)

                    try:

                        delta_w_bias_arr[i-1][k] += delta_w_bias

                    except IndexError:

                        delta_w_bias_arr[i-1].insert(k, delta_w_bias)

                    if (iteration+1) % batch == 0:

                        neur_arr[i-1][k].update_weight(j, round(delta_w_arr[i-1][k], 3))

                        neur_arr[i-1][k].update_bias(round(delta_w_bias_arr[i-1][k], 3))

                        delta_w_arr[i-1][k] = 0

                        delta_w_bias_arr[i-1][k] = 0

                    k += 1

                j += 1

            i -= 1

    return delta_w_arr, delta_w_bias_arr


