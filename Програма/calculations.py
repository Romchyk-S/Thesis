# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 16:14:05 2022

@author: romas
"""

import learning_algorithms as la

import matplotlib.pyplot as plt


def calculate_layer(curr_layer, next_layer, in_arr, learning_algorithm):

        res = []

        i = 0

        while i < len(curr_layer):

            j = 0

            weight_arr = curr_layer[i].get_weights()

            while j < len(weight_arr):

                exit_value = weight_arr[j] * in_arr[i]

                curr_layer[i].set_exit_value(j, exit_value)

                curr_layer[i].update_S(exit_value)

                if i == 0:

                    res.insert(j, exit_value)

                else:

                    res[j] += exit_value

                j += 1

            i += 1

        j = 0

        while j < len(res):

            res[j] = next_layer[j].get_activation_function_value(res[j]+next_layer[j].get_bias())

            j += 1

        return res

def calculate_result(neur_arr, in_arr, learning_algorithm):

    i = 0

    while i < len(neur_arr)-1:

        in_arr = calculate_layer(neur_arr[i], neur_arr[i+1], in_arr, learning_algorithm)

        i += 1

    return in_arr

def calculate_error(exp_res, res, learning_algorithm):

    i = 0

    err = 0

    err_arr = []

    while i < len(exp_res):

        diff = exp_res[i]-res[i]

        err += diff

        if learning_algorithm == 0:

            err_arr.append(diff)

        i += 1

    if learning_algorithm == 0:

        return err, err_arr

    else:

        return err

def calculating_cycle(set_data, set_res, neur_arr, learning_algorithm):

    result = calculate_result(neur_arr, set_data, learning_algorithm)

    if learning_algorithm == 0:

        error, error_arr = calculate_error(set_res, result, learning_algorithm)

        return result, error, error_arr

    else:

        error = calculate_error(set_res, result, learning_algorithm)

        return result, error

def learning_cycle(neur_arr, neur_layer_arr, set_data, set_res, eta, batch, learning_algorithm, *args):

    result = []

    i = 0

    while i < len(set_data):

        err_for_backprop = []

        if learning_algorithm == 0:

            res, error_for_i, err_for_backprop = calculating_cycle(set_data[i], set_res[i], neur_arr, learning_algorithm)

        else:

            res, error_for_i = calculating_cycle(set_data[i], set_res[i], neur_arr, learning_algorithm)

        error_for_i = round(error_for_i, 6)

        result.append(res)

        if i == 0:

            error = error_for_i**2

        else:

            error += error_for_i**2

        if learning_algorithm == 0:

            delta_w, delta_w_bias = la.backpropagation(neur_arr, result, eta, err_for_backprop, batch, i, args[0], args[1])

            for n in neur_arr:

                for m in n:

                    m.set_S(0)

        if (i+1)%batch == 0 and learning_algorithm == 1:

            neur_arr = la.genetic(neur_arr, neur_layer_arr, len(set_res), set_data, set_res, args[0], args[1], args[2], args[3], args[4], args[5], args[6])

        i += 1

    error /= 2

    if learning_algorithm == 1:

        return neur_arr, result, error

    return result, error, delta_w, delta_w_bias


def learning_process(error_threshold, epochs_threshold, set_data, set_res, neur_arr, neur_layer_arr, eta, batch, learning_algorithm, *args):

    error = 1

    err_arr = []

    delta_w = []

    delta_w_bias = []

    count = 0

    if learning_algorithm == 0:

        for n in neur_arr:

            temp_arr = []

            for m in n:

                temp_arr.append(0)

            delta_w.append(temp_arr)

            delta_w_bias.append(temp_arr)


    while error > error_threshold and count < epochs_threshold:

        if learning_algorithm == 0:

            result, error, delta_w, delta_w_bias = learning_cycle(neur_arr, neur_layer_arr, set_data, set_res, eta, batch, learning_algorithm, delta_w, delta_w_bias)

        else:

            neur_arr, result, error = learning_cycle(neur_arr, neur_layer_arr, set_data, set_res, eta, batch, learning_algorithm, args[0], args[1], args[2], args[3], args[4], args[5], args[6])

        err_arr.append(error)

        count += 1

    return result, neur_arr, err_arr

def calculate_set_res(neur_arr, set_data, set_res):

    result = []

    i = 0

    while i < len(set_data):

        res, error_for_i = calculating_cycle(set_data[i], set_res[i], neur_arr, 1)

        error_for_i = round(error_for_i, 6)

        result.append(res)

        if i == 0:

            error = error_for_i**2

        else:

            error += error_for_i**2

        i += 1

    error /= 2

    return result, error

def main_calculation(error_threshold, epochs_threshold, tr_set_data, tr_set_res, test_set_data, test_set_res, neur_arr, neur_layer_arr, eta, batch, learning_algorithm, *args):

    in_parm_for_graph = 1


    if learning_algorithm == 0:

        print("Алгоритм зворотного поширення помилки")

    elif learning_algorithm == 1:

        print("Генетичний алгоритм")


    if learning_algorithm == 0:

        tr_res, neur_arr, tr_err_arr = learning_process(error_threshold, epochs_threshold, tr_set_data, tr_set_res, neur_arr, neur_layer_arr, eta, batch, learning_algorithm)

    else:

        tr_res, neur_arr, tr_err_arr = learning_process(error_threshold, epochs_threshold, tr_set_data, tr_set_res, neur_arr, neur_layer_arr, eta, batch, learning_algorithm, args[0], args[1], args[2], args[3], args[4], args[5], args[6])


    tr_err = tr_err_arr[-1]

    tr_res, tr_err = calculate_set_res(neur_arr, tr_set_data, tr_set_res)

    tr_err_arr.append(tr_err)


    i = 0

    while i < len(tr_res):

        j = 0

        while j < len(tr_res[i]):

            tr_res[i][j] = round(tr_res[i][j], 6)

            j += 1

        i += 1


    print()

    print("Навчальна вибірка")

    print(f"Похибка: {tr_err}")

    print()


    plt.figure(1+learning_algorithm*3)

    plt.title(f"Навчальна вибірка, похибка {tr_err}")

    i = 0

    while i < len(tr_res):

        plt.scatter(tr_set_data[i][in_parm_for_graph], tr_set_res[i], c = "red")

        plt.scatter(tr_set_data[i][in_parm_for_graph], tr_res[i], c = "blue")

        i += 1

    plt.legend(["Очікуваний результат" , "Отриманий результат"], loc = "upper right")

    plt.show()


    plt.figure(2+learning_algorithm*3)


    if learning_algorithm == 0:

        plt.title("Крива навчання мережі зворотним поширенням помилки")

    elif learning_algorithm == 1:

        plt.title("Крива навчання мережі генетичним алгоритмом")



    i = 0

    x = []

    while i < len(tr_err_arr):

        x.append(i)

        i += 1


    plt.plot(x, tr_err_arr)

    plt.show()


    print("Тестова вибірка")

    test_res, test_err = calculate_set_res(neur_arr, test_set_data, test_set_res)

    i = 0

    while i < len(test_res):

        j = 0

        while j < len(test_res[i]):

            test_res[i][j] = round(test_res[i][j], 6)

            j += 1

        i += 1


    print(f"Похибка: {test_err}")

    print()


    plt.figure(3+learning_algorithm*3)

    plt.title(f"Тестова вибірка, похибка {test_err}")

    i = 0

    while i < len(test_res):

        plt.scatter(test_set_data[i][in_parm_for_graph], test_set_res[i], c = "red")

        plt.scatter(test_set_data[i][in_parm_for_graph], test_res[i], c = "blue")

        i += 1

    plt.legend(["Очікуваний результат" , "Отриманий результат"], loc = "upper right")

    plt.show()