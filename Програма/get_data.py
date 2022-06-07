# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:13:44 2022

@author: romas
"""

import numpy as np

import inspect as insp

import activation_functions as af


def get_dataset(file_name):

    f = open(f"{file_name}.txt")

    data = []

    res = []

    for row in f:

        new_row = row.strip().split(" ")

        i = 0

        while i < len(new_row):

            new_row[i] = float(new_row[i])

            if i == 0:

                temp_arr = []

                temp_arr.append(new_row[i])

            elif i == 1:

                temp_arr.append(new_row[i])

            elif i == 2:

                res.append([new_row[i]])

            i += 1

        data.append(temp_arr)

    return data, res


def normalise(set_list):

        upper = 1

        lower = 0

        set_list = np.matrix(set_list).T

        i = 0

        while i < len(set_list):

            max_value = np.amax(set_list[i])

            min_value = np.amin(set_list[i])

            j = 0

            while j < set_list[i].size:

                set_list[i, j] = round(((set_list[i, j] - min_value)/(max_value-min_value)) * (upper-lower) + lower, 6)

                j += 1

            i += 1

        set_list = set_list.T.tolist()

        return set_list


def this_is_evil(set_list_1, set_list_2):

    i = 0

    while i < len(set_list_2):

        j = 0

        while j < len(set_list_2[i]):

            if set_list_2[i][j] >= 0.14:

                del set_list_1[i]

                del set_list_2[i]

                i -= 1

            j += 1

        i += 1


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