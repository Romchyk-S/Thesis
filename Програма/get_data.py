# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 15:13:44 2022

@author: romas
"""

import random as r

def get_dataset(length, entered_parms):

    data = []

    exp_res = []

    i = 0


    a = 0

    b = 1

    # неправильно обчислює, якщо значення не з [0;1].
    # Теоретично врятує нормалізація, однак на практиці нормалізують не лише до проміжку [0;1]
    # Можливо винна активаційна функція

    while i < length:

        D = []

        R = []

        j = 0

        while j < entered_parms:

            D.append(round(a + r.random() * (b-a), 3))

            j += 1

        R.append(round(a + r.random() * (b-a), 3))

        data.append(D)

        exp_res.append(R)

        i += 1

    return data, exp_res