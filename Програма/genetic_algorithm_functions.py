# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:18:44 2022

@author: romas
"""

import create_network as cn

import calculations as c

import random as r



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

def make_chromosome(neur_arr):

    chromosome = []

    for i in neur_arr:

        for j in i:

            k = j.get_weights()

            for m in k:

                chromosome.append(m)

    return chromosome

def create_chromosome_error_dict(initial_population, set_length, set_data, set_res):

    # err_arr = []

    res_arr = []

    population_with_err = {}

    chromosomes = []


    for i in initial_population:

        new_chromosome = make_chromosome(i)

        chromosomes.append(new_chromosome)

        res, err = c.calculating_cycle(set_length, set_data, set_res, i)

        res_arr.append(res)

        population_with_err[tuple(new_chromosome)] = err # потім тут буде хромосома з ваг. Можливо треба внормування err

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


def parent_selection(population):

    # roulette wheel selection

    print(population)

    print()

    normalized_fitness_population = norm_fitness(population)

    print(normalized_fitness_population)

    # тут обирати елементи значення з list(normalized_fitness_population.keys()) з певною ймовірністю list(normalized_fitness_population.values())

    return 0

def crossover(parent_1, parent_2):

    return 0

def mutation(chromosome):

    return 0
