# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

import genetic_algorithm_functions as ga

import calculations as c

# import random as r


def backpropagation_calculation(error_threshold, set_length, set_data, set_res, neur_arr, eta):

    error = 1

    while error > error_threshold:

        result, error = c.calculating_cycle(set_length, set_data, set_res, neur_arr)

        backpropagation_learning(neur_arr, set_res, result, eta)

    return result, error

def backpropagation_learning(neur_arr, exp_res, res, eta):

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

def genetic(neur_arr, neur_layer_arr, set_length, set_data, set_res, err_threshold):

    error = 1

    while error > err_threshold:

        initial_population_length = 10

        initial_population = ga.create_initial_population(initial_population_length, neur_arr, neur_layer_arr)

        # print(initial_population)


        population_with_err = ga.create_chromosome_error_dict(initial_population, set_length, set_data, set_res)

        print(population_with_err)


        # ці ще не працюють


        # ga.parent_selection(population_with_err)


        # crossover_prob = 0 + r.random() * (1-0)

        # if crossover_prob > 0.1:

        #     ga.crossover()

        # mutation_prob = 0 + r.random() * (1-0)

        # if mutation_prob > 0.1:

        #     ga.mutation()

        # чи зберігати батьків?

        # оновити population_with_err, утворити нове покоління

        print()

        err = min(list(population_with_err.values()))

        print(err)

        break

    return 0