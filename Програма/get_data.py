# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:13:44 2022

@author: romas
"""

# import random as r

import numpy as np

from sklearn import datasets

import inspect as insp

import activation_functions as af

def get_dataset(in_parms):

    iris = datasets.load_iris()

    set_data = iris.data[:, :in_parms]  # we only take the first {in_parms} features.

    set_res_temp = iris.target

    set_res = []


    i = 0

    while i < len(set_res_temp):

        set_res.append([set_res_temp[i]])

        i += 1



    upper = 2

    lower = 0

    set_data = np.matrix(set_data).T

    i = 0

    while i < len(set_data):

        max_value = np.amax(set_data[i])

        min_value = np.amin(set_data[i])

        j = 0

        while j < set_data[i].size:

            set_data[i, j] = round(((set_data[i, j] - min_value)/(max_value-min_value)) * (upper-lower) + lower, 3)

            j += 1

        i += 1


    set_data = set_data.T.tolist()


    tr_set_data = set_data[::2]

    tr_set_res = set_res[::2]

    test_set_data = set_data[1::2]

    test_set_res = set_res[1::2]

    return tr_set_data, tr_set_res, test_set_data, test_set_res

def get_activation_funcs():

    functions_list = insp.getmembers(af, insp.isfunction)

    activ_funcs = []

    activ_funcs_ders = []

    i = 0

    while i < len(functions_list):

        if i%2 == 0:

            activ_funcs.append(functions_list[i][1])

        else:

            activ_funcs_ders.append(functions_list[i][1])

        i += 1

    return activ_funcs, activ_funcs_ders