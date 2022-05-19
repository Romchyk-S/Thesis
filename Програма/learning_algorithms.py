# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

import genetic_algorithm_functions as ga

import random as r


def backpropagation(neur_arr, res, eta, err):

    # як оновлювати bias?

    j = len(neur_arr)-1

    while j > 0:

        k = 0

        while k < len(neur_arr[j]):

            if j == len(neur_arr)-1:

                neur_arr[j][k].set_error(err)

            else:

                l = 0

                while l < len(neur_arr[j+1]):

                    # можливо, треба буде значення f_der, тоді neur_arr[j][k].set_error(f_der(neur_arr[j][k].get_S())*neur_arr[j][k].get_weight(l)*neur_arr[j+1][l].get_error())

                    neur_arr[j][k].set_error(neur_arr[j][k].get_weight(l)*neur_arr[j+1][l].get_error())

                    l += 1


            f_der = neur_arr[j][k].get_der_value_for_backprop()

            delta_w_temp = neur_arr[j][k].get_error()*f_der

            l = 0

            while l < len(neur_arr[j-1]):

                # якщо ставити batch training, необхідно накопичувати delta_w, мабуть із множеннням на eta,
                # нема сенсу ліпити докупи купу різних речей у calculations
                # тоді всі сетери у класі мають позбутися плюсів
                # потім, коли буде досягнуто значення batch_length, оновлювати ваги
                # приблизний код: delta_w_arr = [[delta_w[0][0], delta_w[0][1]...][delta_w[1][0], delta_w[1][1]...]...[...delta_w[n][n]]]
                # на кожній ітерації delta_w[i][j] += eta*нове delta_w
                # if counter == batch:
                # for i in len(delta_w_arr):
                # for j in len(delta_w_arr[i]):
                # neuron[i][j].set_weight(delta[i][j])
                # delta_w[i][j] == 0


                delta_w = delta_w_temp*neur_arr[j-1][l].get_exit_value(k)

                neur_arr[j-1][l].update_weight(k, eta*delta_w)

                l += 1

            k += 1

        j -= 1

    for n in neur_arr:

        for m in n:

            m.to_zero()

def genetic(neur_arr, neur_layer_arr, set_length, set_data, set_res):

    population_length = 100

    new_population = []


    population_with_err = ga.create_initial_population(population_length, neur_arr, neur_layer_arr, set_length, set_data, set_res)

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

    best_neur_arr = ga.choose_best_network(new_population, neur_arr, set_data, set_res)

    return best_neur_arr