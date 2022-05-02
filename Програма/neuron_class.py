# -*- coding: utf-8 -*-
"""
Created on Fri Apr  8 16:49:15 2022

@author: romas
"""

import random as r

class Neuron:

    index = 0

    layer = 0

    bias = 0

    error = 0


    def __init__ (self, num_ind, num_layer):

        self.index = num_ind

        self.layer = num_layer

        self.weights = []

        self.exit_value = []

        self.bias = round(0 + (r.random() * (1 - 0)), 2)

    def get_layer(self):

        return self.layer

    def add_weights(self, num_next_layer_quant):

        i = 0

        while i < num_next_layer_quant:

            self.weights.append(round(0 + (r.random() * (1 - 0)), 2))

            i += 1

    def update_weight(self, ind, value):

        self.weights[ind] += value

    def set_error(self): # доробити

        return 0

    def get_error(self):

        return self.error

    def set_exit_value(self, ind): # доробити

        return 0

    def get_exit_value(self, ind):

        return self.exit_value[ind]


    def get_weights(self):

        return self.weights

    def get_bias(self):

        return self.bias

    def __repr__(self):

        return f"{self.index}_{self.layer}"