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

    def add_random_weights(self, next_layer_quant):

        i = 0

        while i < next_layer_quant:

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

    def update_bias(self, value):

        self.bias += value

    def set_bias(self, value):

        self.bias = value

    def set_error(self, value):

        self.error += value

    def get_error(self):

        return self.error

    def get_exit_values(self):

        return self.exit_values

    def set_exit_value(self, ind, value):

        try:

            self.exit_values[ind] += value

        except IndexError:

            self.exit_values.insert(ind, value)

    def get_exit_value(self, ind):

        return self.exit_values[ind]

    def update_S(self, value):

        self.S += value

    def set_S(self, value):

        self.S = value

    def get_S(self):

        return self.S

    def set_activation_function(self, func):

        self.activ_func = func

        self.activ_func_der = 0 # Теж подумати

    def get_activation_function_value(self, x): # обрати якусь кращу, можливо певним чином комбінувати різні для різних рівнів

        #Leaky ReLU

        # if x < 0:

        #     return 0.01*x

        # else:

        #     return x

        return (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))

        # return self.activ_func(x)

    def get_activation_function_der_value(self, x):


        # if x < 0:

        #     return 0.01

        # else:

        #     return 1

        # return 1 - (round((m.exp(x) - m.exp(-x)), 3)**2/(round((m.exp(x) + m.exp(-x)), 3)**2))

        try:

            return 1 - (((m.exp(x) - m.exp(-x))**2)/((m.exp(x) + m.exp(-x))**2))

        except OverflowError:

            print(self.get_weights())

            print(x)

            print()

        # return self.activ_func_der(x)

    def set_der_value_for_backprop(self, x):

        self.der_value_for_backprop += self.get_activation_function_der_value(x)

    def get_der_value_for_backprop(self):

        return self.der_value_for_backprop

    def to_zero(self):

        self.error = 0

        self.der_value_for_backprop = 0

        self.S = 0

        self.exit_values = []