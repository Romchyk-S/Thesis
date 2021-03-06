# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

import backpropagation_functions as bf

import genetic_algorithm_functions as ga

def backpropagation(neur_arr, res, eta, err, batch, iteration, delta_w_arr, delta_w_bias_arr):

    bf.set_errors(neur_arr, err)

    delta_w_arr, delta_w_bias_arr = bf.update_delta_w(neur_arr, eta, delta_w_arr, delta_w_bias_arr, iteration, batch)

    for n in neur_arr:

        for m in n:

            m.to_zero()

    return delta_w_arr, delta_w_bias_arr

def genetic(neur_arr, neur_layer_arr, set_length, set_data, set_res, w_bottom, w_upper, func_arr, func_der_arr, crossover_prob, mutation_prob, population_length):

    new_population = []

    population_with_err = ga.create_initial_population(population_length, neur_arr, neur_layer_arr, set_length, set_data, set_res, w_bottom, w_upper, func_arr, func_der_arr)

    normalized_fitness_population = ga.norm_fitness(population_with_err)


    while len(new_population) < population_length:

        chromosome_1, chromosome_2 = ga.offsprings_creation(normalized_fitness_population, w_bottom, w_upper, crossover_prob, mutation_prob)

        new_population.append(chromosome_1)

        new_population.append(chromosome_2)

    best_neur_arr = ga.choose_best_network(new_population, neur_arr, set_data, set_res)

    return best_neur_arr