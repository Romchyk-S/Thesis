# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

import genetic_algorithm_functions as ga

import calculations as c

import random as r


def backpropagation_calculation(error_threshold, set_data, set_res, neur_arr, eta, batch):

    print()

    error = 1

    err_for_backprop = 0

    count = 0


    while error > error_threshold:

        result = []

        i = 0

        while i < len(set_data):

            res, error_for_i = c.calculating_cycle(set_data[i], set_res[i], neur_arr)

            if i == batch:

                backpropagation_learning(neur_arr, result, eta, err_for_backprop)

            # res[0] = res[0]

            error_for_i = round(error_for_i, 3)

            result.append(res)

            if i == 0:

                try:

                    error = error_for_i**2

                    err_for_backprop = error_for_i

                except OverflowError:

                    print("err_i")

                    print(error_for_i)

                    break

            else:

                error += error_for_i**2

                err_for_backprop += error_for_i

            i += 1

        error /= len(set_res)

        # error *= 1/2

        # if count%100 == 0:

        #     # print(neur_arr[0][0].get_weights())

        #     print("error")

        #     print(error)

        #     print()

        #     # print("error_for_backprop")

        #     # print(err_for_backprop)

        #     print("result")

        #     print(result)

        #     # print()

        # if count >= 10000:

        #     break

        count += 1

    return result, error, count

def backpropagation_learning(neur_arr, res, eta, err):

    # як оновлювати bias?

    i = 0

    while i < len(res):

        j = len(neur_arr)-1

        while j > 0:

            k = 0

            while k < len(neur_arr[j]):

                if j == len(neur_arr)-1:

                    # print("Here is error")

                    # print(neur_arr[j][k].get_error())

                    neur_arr[j][k].set_error(err)

                    # print(neur_arr[j][k].get_error())

                    # print()

                else:

                    l = 0

                    while l < len(neur_arr[j+1]):

                        neur_arr[j][k].set_error(neur_arr[j][k].get_weight(l)*neur_arr[j+1][l].get_error())

                        l += 1


                f_der = neur_arr[j][k].get_der_value_for_backprop()

                # print("delta_w_temp")

                # print(neur_arr[j][k].get_error())

                # print(f_der)

                delta_w_temp = neur_arr[j][k].get_error()*f_der


                l = 0

                while l < len(neur_arr[j-1]):

                    # print(delta_w_temp)

                    delta_w = delta_w_temp*neur_arr[j-1][l].get_exit_value(k)

                    # print(delta_w)

                    # print(-eta*delta_w)

                    # print(neur_arr[j-1][l].get_weight(k))

                    neur_arr[j-1][l].update_weight(k, eta*delta_w)

                    # print(neur_arr[j-1][l].get_weight(k))

                    # print()

                    l += 1


                k += 1

            j -= 1

        i += 1

        for n in neur_arr:

            for m in n:

                m.to_zero()

def genetic(neur_arr, neur_layer_arr, set_length, set_data, set_res, err_threshold):

    count = 0

    population_length = 100

    population_with_err = ga.create_initial_population(population_length, neur_arr, neur_layer_arr, set_length, set_data, set_res)

    err = min(list(population_with_err.values()))



    while err > err_threshold:

        new_population = []

        normalized_fitness_population = ga.norm_fitness(population_with_err) # формулу всередині потрібно виправити


        while len(new_population) < population_length:

            chromosome_1, chromosome_2 = ga.parent_selection(normalized_fitness_population)

            crossover_prob = 0 + r.random() * (1-0)

            if crossover_prob > 0.1:

                chromosome_1, chromosome_2 = ga.crossover(chromosome_1, chromosome_2)


            mutation_prob = 0 + r.random() * (1-0)

            if mutation_prob > 0.1:

                chromosome_1 = ga.mutation(chromosome_1)


            mutation_prob = 0 + r.random() * (1-0)

            if mutation_prob > 0.1:

                chromosome_2 = ga.mutation(chromosome_2)


            new_population.append(chromosome_1)

            new_population.append(chromosome_2)

        # батьки збережуться, якщо не випаде ні мутація, ні схрещування

        population = new_population.copy()

        population_with_err = {}

        i = 0

        while i < len(population):

          new_neur_arr = ga.create_new_network(list(new_population[i]), neur_arr)

          res, err = c.calculating_cycle(set_length, set_data, set_res, new_neur_arr)

          population_with_err[population[i]] = err

          i += 1

        # print(len(population_with_err))

        # print()

        err = min(list(population_with_err.values()))

        count += 1

        break

    print(err)

    return err