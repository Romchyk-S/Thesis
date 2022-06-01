# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:49:15 2022

@author: romas
"""

import random as r

# import activation_functions as af

class Neuron:

    index = 0

    layer = 0

    bias = 0

    error = 0

    S = 0

    activ_func = 0

    activ_func_der = 0

    def __init__ (self, num_ind, num_layer, func, func_der, *args):

        self.index = num_ind

        self.layer = num_layer

        if self.layer != 0 and len(args) > 0:

            bias_bottom = args[0]

            bias_upper = args[1]

            self.bias = round(bias_bottom + (r.random() * (bias_upper - (bias_bottom))), 3)

        self.weights = []

        self.exit_values = []

        self.activ_func = func

        self.activ_func_der = func_der

    def __repr__(self):

        return f"{self.index}_{self.layer}"

    def get_index(self):

        return self.index

    def get_layer(self):

        return self.layer

    def add_random_weights(self, next_layer_quant, *args):

        if len(args) > 0:

            w_bottom = args[0]

            w_upper = args[1]

        else:

            w_bottom = -1

            w_upper = 1

        i = 0

        while i < next_layer_quant:

            self.weights.append(round(w_bottom + (r.random() * (w_upper - (w_bottom))), 3))

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

    def set_activation_function_der(self, func):

        self.activ_func_der = func

    def get_activation_function(self):

        return self.activ_func

    def get_activation_function_der(self):

        return self.activ_func_der

    def get_activation_function_value(self, x):

        return self.activ_func(x)

    def get_activation_function_der_value(self, x):

        return self.activ_func_der(x)

    def to_zero(self):

        self.error = 0

        self.S = 0

        self.exit_values = []