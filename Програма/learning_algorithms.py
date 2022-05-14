# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

import genetic_algorithm_functions as ga

import calculations as c

import random as r


def backpropagation_calculation(error_threshold, set_length, set_data, set_res, neur_arr, eta):

    error = 1

    count = 0

    while error > error_threshold:

        result, error = c.calculating_cycle(set_length, set_data, set_res, neur_arr)

        backpropagation_learning(neur_arr, set_res, result, eta)

        count += 1

    return result, error, count

def backpropagation_learning(neur_arr, exp_res, res, eta):

    # як оновлювати bias?

    i = 0

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

    count = 0

    population_length = 10

    population = ga.create_initial_population(population_length, neur_arr, neur_layer_arr)

    population_with_err = ga.create_chromosome_error_dict(population, set_length, set_data, set_res)


    while error > err_threshold:

        new_population = []

        normalized_fitness_population = ga.norm_fitness(population_with_err) # формулу всередині потрібно виправити


        while len(new_population) < population_length:

            chromosome_1, chromosome_2 = ga.parent_selection(normalized_fitness_population)

            print(chromosome_1)

            print(chromosome_2)

            print()

            # для тесту роботи, у фінальному коді не буде

            chromosome_1, chromosome_2 = ga.crossover(chromosome_1, chromosome_2)

            print(chromosome_1)

            print(chromosome_2)

            print()

            break


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

        break

        population = new_population

        population_with_err = ga.create_chromosome_error_dict(population, set_length, set_data, set_res)

        err = min(list(population_with_err.values()))

        print(err)

        count += 1

        break

    # як розділяти найкращу хромосому для утворення нової мережі, чи зберігати декілька з них і запускати на їх базі навчання зворотним поширенням помилки

    return 0