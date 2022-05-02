# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:54:48 2022

@author: romas
"""

def backpropagation(neur_arr, exp_res, res, eta, activation_func):


    # фіксуємо останній рівень. Цикл 1. i = len(neur_arr)-1, i > 0
    # Записуємо вихід першого нейрона (n) на ньому, порівнюємо з очікуваним. set_error(self, num) Беремо похідну функції активації в точці індукованого локального поля (activ_func_der). Для збереження індукованого локального поля нові функції класу set_S, get_S. Цикл 2. j = 0, j < len(neur_arr[i])
    # Фіксуємо всі нейрони, що входять у нейрон вихідного рівня.  Цикл 3. k = 0. k < len(neur_arr[i-1]). Тому не треба, аби нейрон вихідного рівня щось бачив
    # Множимо похибку n на вхід, наданий кожним розглянутим нейроном, оновлюємо вагу. neur_arr[i-1][k].update_weight(j, (neur_arr[i][j].get_error())*neur_arr[i-1][k].get_exit_value(self, j)*activ_func_der(S)). Для цього треба зберігати виходи в циклі обчислення, нові функції класу set_exit_value та get_exit_value, а також update_weight
    # Коли той цикл за k завершено, нейрон ij надсилає кожному нейрону попереднього рівня сигнал.  Цикл 4. k = 0. k < len(neur_arr[i-1]). Надіслати кожному з них (d-y)*neur_arr[i-1][k].get_weight(j), вага оновлена внаслідок навчання. neur_arr[i-1][k].set_error(надісланий результат). set_error(self, num): self.error + num, нові функції класу set_error та get_error
    # Перейти на i -= 1
    # Необхідні функції класу: set_S, get_S, get_error, set_error, set_exit_value, get_exit_value, update_weight(j)
    # Результат: 4 цикли, 7 нових функцій класу, відповідні їм 3 параметри, обчислення похідної активаційної функції. Можливо, ще один параметр класу та відповідні функції до нього

    # i = 0

    # while i < len(exp_res): # по всій вибірці

    #     j = 0

    #     while j < len(res): # по локальному полю / вектору різниць

    #         k = 0

    #         while k < len()

    #         j += 1

    #     i += 1

    return 0

def genetic(neur_arr, desired_result, current_result):

    return 0