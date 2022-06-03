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

import math as m

def get_data(file_name):

    f = open(f"{file_name}.txt")

    R = []

    Y = []

    A = []

    delta_K = []

    growth = []

    for row in f:

        new_row = row.strip().split(" ")

        i = 0

        while i < len(new_row):

          new_row[i] = float(new_row[i])

          if i == 0:

              R.append(new_row[i])

          elif i == 1:

              delta_K.append(new_row[i])

              A.append([1, m.log(new_row[i])])

          elif i == 2:

              growth.append(new_row[i])

              Y.append(m.log(new_row[i]))

          i += 1

    A = np.matrix(A)

    Y = np.matrix(Y)

    beta = ((A.T*A)**-1*A.T)*Y.T

    beta = beta.tolist()

    beta[0][0] = m.exp(beta[0][0])

    f.close()

    return R[0], beta[0], beta[1], delta_K, growth

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


# def get_dataset(in_parms):

#     iris = datasets.load_iris()

#     set_data = iris.data[:, :in_parms]  # we only take the first {in_parms} features.

#     set_res_temp = iris.target

#     set_res = []


#     i = 0

#     while i < len(set_res_temp):

#         set_res.append([set_res_temp[i]])

#         i += 1



#     upper = 2

#     lower = 0

#     set_data = np.matrix(set_data).T

#     i = 0

#     while i < len(set_data):

#         max_value = np.amax(set_data[i])

#         min_value = np.amin(set_data[i])

#         j = 0

#         while j < set_data[i].size:

#             set_data[i, j] = round(((set_data[i, j] - min_value)/(max_value-min_value)) * (upper-lower) + lower, 3)

#             j += 1

#         i += 1


#     set_data = set_data.T.tolist()


#     tr_set_data = set_data[::2]

#     tr_set_res = set_res[::2]

#     test_set_data = set_data[1::2]

#     test_set_res = set_res[1::2]

#     return tr_set_data, tr_set_res, test_set_data, test_set_res

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