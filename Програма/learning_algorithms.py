# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

# import genetic_algorithm_functions as ga


def backpropagation(neur_arr, exp_res, res, eta):

    # як оновлювати bias?

    i = 0

    # i->j, j->k, k->l

    while i < len(res):

        j = len(neur_arr)-1

        while j > 0:

            k = 0

            while k < len(neur_arr[j]):

                if j == len(neur_arr)-1:

                    neur_arr[j][k].set_error(exp_res[i][k]-res[i][k])

                else:

                    l = 0

                    while l < len(neur_arr[j+1]):

                        neur_arr[j][k].set_error(neur_arr[j][k].get_weight(l)*neur_arr[j+1][l].get_error())

                        l += 1

                # зберегли помилку
                # похідна функції активації в точці

                f_der = neur_arr[j][k].get_activation_function_der_value(neur_arr[j][k].get_S())

                delta_w_temp = eta*neur_arr[j][k].get_error()*f_der


                # знайти значення, яке нейрон передав на наступний рівень, оновити вагу

                l = 0

                while l < len(neur_arr[j-1]):

                    delta_w = delta_w_temp*neur_arr[j-1][l].get_exit_value(k)

                    # print(j-1)

                    # print(l)

                    # print(delta_w)

                    # print()

                    neur_arr[j-1][l].update_weight(k, delta_w)

                    l += 1


                k += 1

            j -= 1

        i += 1

    return 0

def genetic(neur_arr, exp_res, res):

    return 0