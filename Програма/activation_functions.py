# -*- coding: utf-8 -*-
"""
Created on Tue May  3 13:04:24 2022

@author: romas
"""

import math as m



alpha_lin = 2

alpha_ReLU = 0.1

alpha_ELU = 0.2

alpha_SELU = 1.2

lambda_SELU = 0.1


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

def ReLU_x6(x):

    return min(max(0,x), 6)

def Relu_x6_der(x):

    if x < 0 or x > 6:

        return 0

    return 1

def Leaky(x):

    if x < 0:

        return alpha_ReLU*x

    else:

        return x

def Leaky_der(x):

    if x < 0:

        return alpha_ReLU

    else:

        return 1

def ELU(x):

    if x < 0:

        return alpha_ELU*(m.exp(x)-1)

    else:

        return x

def ELU_der(x, *args):

    if len(args) == 0:

        a = 1

    else:

        a = lambda_SELU


    if x < 0:

        return a*alpha_ReLU*m.exp(x)

    else:

        return a

def SELU(x):

    if x < 0:

        return lambda_SELU * (alpha_SELU*m.exp(x) - alpha_SELU)

    else:

        return lambda_SELU * x

def SELU_der(x):

    return ELU_der(x, x)

def Sigmoid(x):

    # print(x)

    return 1/(1+m.exp(-x))

def Sigmoid_der(x):

    return Sigmoid(x)*(1-Sigmoid(x))

def Tanh(x):

    return (m.exp(x) - m.exp(-x))/(m.exp(x) + m.exp(-x))

def Tanh_der(x):

    return 1 - (Tanh(x)**2)

def Softplus(x):

    # try:

        return m.log(1+m.exp(x))

    # except OverflowError:

    #     print(x)

def Softplus_der(x):

    return Sigmoid(x)

# def softmax(x):

#     return x

# def softmax_der(x):

#     return x