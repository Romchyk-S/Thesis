# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:49:15 2022

@author: romas
"""

import random as r

import math as m

# import activation_functions as af

class Neuron:

    index = 0

    layer = 0

    bias = 0

    error = 0

    S = 0

    der_value_for_backprop = 0

    activ_func = 0 # подумати, як передавати її. Можливо масив функцій


    def __init__ (self, num_ind, num_layer):

        self.index = num_ind

        self.layer = num_layer

        # self.bias = round(0 + (r.random() * (1 - 0)), 2)

        self.bias = 0 # не знаю, як оновлювати, тимчасово відключив

        self.weights = []

        self.exit_values = []

    def __repr__(self):

        return f"{self.index}_{self.layer}"

    def get_index(self):

        return self.index

    def get_layer(self):

        return self.layer

    def add_random_weights(self, num_next_layer_quant):

        i = 0

        while i < num_next_layer_quant:

            self.weights.append(round(0 + (r.random() * (1 - 0)), 2))

            i += 1

    def add_weights_from_arr(self, weight_arr):

        i = 0

        while i < len(weight_arr):

            self.weights.append(weight_arr[i])

            i += 1

    def get_weight(self, ind):

        return self.weights[ind]

    def get_weights(self):

        return self.weights

    def update_weight(self, ind, value):

        self.weights[ind] += value

    def get_bias(self):

        return self.bias

    def set_error(self, value):

        self.error += value

    def get_error(self):

        return self.error

    def set_exit_value(self, ind, value):

        try:

            self.exit_values[ind] += value

        except IndexError:

            self.exit_values.insert(ind, value)

    def get_exit_value(self, ind):

        return self.exit_values[ind]

    def set_S(self, value):

        self.S = value

    def get_S(self):

        return self.S

    def get_activation_function_value(self, x): # обрати якусь кращу, можливо певним чином комбінувати різні для різних рівнів



        #Leaky ReLU

        # if x < 0:

        #     return 0.01*x

        # else:

        #     return x

        return (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))

    def get_activation_function_der_value(self, x):

        # print(x)

        # x = round(x, 3)

        # print(x)

        # print(m.exp(x))

        # print(m.exp(-x))

        # print(m.exp(x) - m.exp(-x))

        # print(m.exp(x) + m.exp(-x))

        # print()

        # if x < 0:

        #     return 0.01

        # else:

        #     return 1

        # return 1 - (round((m.exp(x) - m.exp(-x)), 3)**2/(round((m.exp(x) + m.exp(-x)), 3)**2))

        return 1 - (((m.exp(x) - m.exp(-x))**2)/((m.exp(x) + m.exp(-x))**2))

    def set_der_value_for_backprop(self, x):

        self.der_value_for_backprop += self.get_activation_function_der_value(x)

    def get_der_value_for_backprop(self):

        return self.der_value_for_backprop

    def to_zero(self):

        self.error = 0

        self.der_value_for_backprop = 0

        self.S = 0

        i = 0

        while i < len(self.exit_values):

            self.exit_values[i] = 0

            i += 1


