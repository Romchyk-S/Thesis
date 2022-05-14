# -*- coding: utf-8 -*-
"""
Created on Tue May  3 10:18:44 2022

@author: romas
"""

import create_network as cn

import calculations as c

import random as r

import numpy as np



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

    chromosome = ()

    for i in neur_arr:

        for j in i:

            k = j.get_weights()

            for m in k:

                chromosome += (m, )

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

        population_with_err[new_chromosome] = err

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

    parents = r.choices(list(population.keys()), weights = list(population.values()), k = 2)

    return parents

def crossover(chromosome_1, chromosome_2):

    len_crossover = r.randint(1, round(len(chromosome_1)/2))

    quant_crossover = r.randint(1, round(len(chromosome_1)/(2*len_crossover)))

    chromosome_1 = np.array_split(chromosome_1, round(len(chromosome_1)/(len_crossover)))

    chromosome_2 = np.array_split(chromosome_2, round(len(chromosome_2)/(len_crossover)))

    i = 0

    while i < quant_crossover:

        ind = r.randint(0, len(chromosome_1)-1)

        temp = chromosome_1[ind]

        chromosome_1[ind] = chromosome_2[ind]

        chromosome_2[ind] = temp

        i += 1

    i = 1

    while i < len(chromosome_1):

        chromosome_1[0] = np.concatenate((chromosome_1[0], chromosome_1[i]))

        chromosome_2[0] = np.concatenate((chromosome_2[0], chromosome_2[i]))

        del chromosome_1[i]

        del chromosome_2[i]

    chromosome_1 = tuple(map(tuple, chromosome_1))[0]

    chromosome_2 = tuple(map(tuple, chromosome_2))[0]

    return chromosome_1, chromosome_2

def mutation(chromosome):

    # обрати тип або їх комбінацію

    return chromosome
