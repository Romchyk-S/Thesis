# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:18:44 2022

@author: romas
"""

import create_network as cn

import calculations as c



def create_initial_population(initial_population_length, neur_arr, neur_layer_arr):

    initial_population = []

    i = 0

    while i < initial_population_length:

        if i == 0:

            initial_population.append(neur_arr.copy())

        else:

            initial_population.append(cn.create_neurons(len(neur_arr[0]), len(neur_arr[-1]), len(neur_arr)-2, neur_layer_arr))

        i += 1

    return initial_population

def create_chromosome_error_dict(initial_population, set_length, set_data, set_res):

    # err_arr = []

    res_arr = []

    population_with_err = {}

    chromosomes = []

    for i in initial_population:

        chromosomes.append(make_chromosome(i))

        res, err = c.calculating_cycle(set_length, set_data, set_res, i)

        res_arr.append(res)

        population_with_err[i[0][0]] = err # потім тут буде хромосома з ваг. Можливо треба внормування err

    return population_with_err


def make_chromosome(neur_arr):

    return 0

def parent_selection(population):

    # ideally roulette wheel selection
    # prob_of_choice = 1/err (?)

    return 0

def crossover(parent_1, parent_2):

    return 0

def mutation(chromosome):

    return 0
