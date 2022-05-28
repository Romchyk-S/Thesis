# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:04:24 2022

@author: romas
"""

import math as m



alpha_lin = 2

alpha_LU = 0.1

lambda_LU = 0.01



def Linear(x):

    return alpha_lin*x

def Linear_der(x):

    return alpha_lin

def ReLU(x, *args):

    if x < 0:

        return 0

    else:

        if len(args) > 0:

            return 1

        else:

            return x

def ReLU_der(x):

    return ReLU(x, x)

def Leaky(x):

    if x < 0:

        return alpha_LU*x

    else:

        return x

def Leaky_der(x):

    if x < 0:

        return alpha_LU

    else:

        return 1

def ELU(x):

    if x < 0:

        return alpha_LU*(m.exp(x)-1)

    else:

        return x

def ELU_der(x, *args):

    if len(args) == 0:

        a = 1

    else:

        a = lambda_LU


    if x < 0:

        return a*alpha_LU*m.exp(x)

    else:

        return a*

def SELU(x):

    if x < 0:

        return lambda_LU * (alpha_LU*m.exp(x) - alpha_LU)

    else:

        return lambda_LU * x

def SELU_der(x):

    return ELU_der(x, x)

def sigmoid(x):

    return 1/(1+m.exp(-x))

def sigmoid_der(x):

    return sigmoid(x)*(1-sigmoid(x))

def Tanh(x):

    return (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))

def Tanh_der(x):

    return 1 - (Tanh(x)**2)

def softplus(x):

    return m.log(1+m.exp(x))

def softplus_der(x):

    return sigmoid(x)

# def softmax(x):

#     return x

# def softmax_der(x):

#     return x