# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:18:44 2022

@author: romas
"""

import create_network as cn

import neuron_class as nc

import calculations as c

import random as r

import numpy as np


def make_chromosome(neur_arr):

    chromosome = ()

    for i in neur_arr:

        for j in i:

            k = j.get_weights()

            for m in k:

                chromosome += (m, )

            chromosome += (j.get_bias(), )

    return chromosome

def create_initial_population(initial_population_length, neur_arr, neur_layer_arr, set_length, set_data, set_res, w_bottom, w_upper, func_arr, func_der_arr):

    population_with_err = {}

    i = 0

    while i < initial_population_length:

        err = 0

        if i == 0:

            new_neur_arr = neur_arr.copy()

        else:

            # якщо робити еволюцію у вигляді зміни активаційних функцій, це робити тут, обираючи інші функції зі списку. Але на це нема часу.

            new_neur_arr = cn.create_neurons(len(neur_arr[0]), len(neur_arr[-1]), len(neur_arr)-2, neur_layer_arr, func_arr, func_der_arr, w_bottom, w_upper)

        j = 0

        while j < set_length:

            res, err_for_j = c.calculating_cycle(set_data[j], set_res[j], new_neur_arr, 1)

            err += err_for_j**2

            j += 1

        err /= len(set_res)

        chromosome = make_chromosome(new_neur_arr)

        population_with_err[chromosome] = err

        i += 1

    return population_with_err

def norm_fitness(population):

    fit_arr = list(population.values())

    chromosome_arr = list(population.keys())

    min_fit = min(fit_arr)

    new_dict = {}


    i = 0

    while i < len(fit_arr):

        new_dict[chromosome_arr[i]] = min_fit/fit_arr[i] # подумати над формулою, аби мінімальне значення не мало ймовірності 1

        i += 1

    return new_dict

def parent_selection(normalized_population):

    # roulette wheel selection

    parents = r.choices(list(normalized_population.keys()), weights = list(normalized_population.values()), k = 2)

    return parents

def crossover(chromosome_1, chromosome_2):

    len_crossover = r.randint(1, round(len(chromosome_1)/2))

    quant_crossover = r.randint(1, round(len(chromosome_1)/(2*len_crossover)))

    chromosome_1 = np.array_split(chromosome_1, round(len(chromosome_1)/(len_crossover)))

    chromosome_2 = np.array_split(chromosome_2, round(len(chromosome_2)/(len_crossover)))


    temp_arr = []

    i = 0

    while i < len(chromosome_1):

        temp_arr.append(i)

        i += 1

    ind_arr = r.sample(temp_arr, quant_crossover)


    for i in ind_arr:

        temp = chromosome_1[i]

        chromosome_1[i] = chromosome_2[i]

        chromosome_2[i] = temp


    i = 1

    while i < len(chromosome_1):

        chromosome_1[0] = np.concatenate((chromosome_1[0], chromosome_1[i]))

        chromosome_2[0] = np.concatenate((chromosome_2[0], chromosome_2[i]))

        del chromosome_1[i]

        del chromosome_2[i]



    chromosome_1 = tuple(map(tuple, chromosome_1))[0]

    chromosome_2 = tuple(map(tuple, chromosome_2))[0]

    return chromosome_1, chromosome_2

def mutation(chromosome, w_bottom, w_upper):

    # random resetting

    chromosome = list(chromosome)

    quant_mutation = r.randint(1, round(len(chromosome)/3))

    temp_arr = []

    i = 0

    while i < len(chromosome):

        temp_arr.append(i)

        i += 1

    ind_arr = r.sample(temp_arr, quant_mutation)

    for i in ind_arr:

        chromosome[i] = round(w_bottom + (r.random() * (w_upper - (w_bottom))), 2)

    chromosome = tuple(chromosome)

    return chromosome

def offsprings_creation(normalized_fitness_population, w_bottom, w_upper):

    chromosome_1, chromosome_2 = parent_selection(normalized_fitness_population)

    crossover_prob = 0 + r.random() * (1-0)

    if crossover_prob > 0.1:

        chromosome_1, chromosome_2 = crossover(chromosome_1, chromosome_2)

    mutation_prob = 0 + r.random() * (1-0)

    if mutation_prob > 0.5:

        chromosome_1 = mutation(chromosome_1, w_bottom, w_upper)

    mutation_prob = 0 + r.random() * (1-0)

    if mutation_prob > 0.5:

        chromosome_2 = mutation(chromosome_2, w_bottom, w_upper)

    return chromosome_1, chromosome_2

def create_new_network(chromosome, neur_arr):

    i = 0

    network = []

    for i in neur_arr:

        layer = []

        for j in i:

            weights_num = len(j.get_weights())

            neuron = nc.Neuron(j.get_index(), j.get_layer(), j.get_activation_function(), j.get_activation_function_der())

            neuron.add_weights_from_arr(chromosome[0:weights_num])

            del chromosome[0:weights_num-1]

            neuron.set_bias(chromosome[0])

            del chromosome[0]

            layer.append(neuron)

        network.append(layer)

    return network

def choose_best_network(population, neur_arr, set_data, set_res):

    temp_arr = population.copy()

    population_with_err = {}

    i = 0

    while i < len(temp_arr):

      new_neur_arr = create_new_network(list(temp_arr[i]), neur_arr)

      err = 0

      j = 0

      while j < len(set_res):

          res, err_for_j = c.calculating_cycle(set_data[j], set_res[j], new_neur_arr, 1)

          err += err_for_j**2

          j += 1

      err /= len(set_res)

      population_with_err[population[i]] = err

      i += 1


    dict_values_list = list(population_with_err.values())

    err = min(dict_values_list)

    ind_err = dict_values_list.index(err)

    new_neur_arr = create_new_network(list(population[ind_err]), neur_arr)

    return new_neur_arr

