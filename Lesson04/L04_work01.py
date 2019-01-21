# Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.

import json


# --------------------------------------------------------------------------------------------------------------
# 1. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
# 1.1 Решение вариант 01
def maxmin_for(n):
    """Файл массива генерируеться в generator.py"""
    """ python generator.py n """
    array_file = open('array_gen.py')
    array = json.loads(array_file.read())
    array_file.close()
    x_max = 0
    i_max = 0
    x_min = array[0]
    i_min = 0
    summ = 0
    for i in range(len(array)):
        if x_min > array[i]:
            x_min = array[i]
            i_min = i
        if x_max < array[i]:
            x_max = array[i]
            i_max = i
    if i_min > i_max:
        i_max, i_min = i_min, i_max
    for n in range(i_min + 1, i_max):
        summ += array[n]
    return summ


# 100 loops, best of 3: 124 usec per loop - 10
# 100 loops, best of 3: 124 usec per loop - 20
# 100 loops, best of 3: 144 usec per loop - 100
# 100 loops, best of 3: 237 usec per loop - 500
# 100 loops, best of 3: 695 usec per loop - 2500
# 100 loops, best of 3: 1.27 msec per loop - 5000
# 100 loops, best of 3: 6.1 msec per loop - 25000
# 100 loops, best of 3: 24 msec per loop - 100000
# 100 loops, best of 3: 129 msec per loop - 500000


# 1.2 Решение вариант 02
def maxmin_var02(n):
    array_file = open('array_gen.py')
    array = json.loads(array_file.read())
    array_file.close()
    x_max = max(array)
    x_min = min(array)
    i_max = array.index(x_max)
    i_min = array.index(x_min)
    if i_min > i_max:
        i_max, i_min = i_min, i_max
    return x_max, i_max, x_min, i_min, sum(array[i_min + 1: i_max])

# 100 loops, best of 3: 116 usec per loop - 10
# 100 loops, best of 3: 121 usec per loop - 20
# 100 loops, best of 3: 136 usec per loop - 100 (быстрее в 1.05 раз)
# 100 loops, best of 3: 209 usec per loop - 500 (быстрее в 1.33 раз)
# 100 loops, best of 3: 508 usec per loop - 2500 (быстрее в 1.37 раз)
# 100 loops, best of 3: 1.04 msec per loop - 5000 (быстрее в 1.22 раз)
# 100 loops, best of 3: 4.14 msec per loop - 25000 (быстрее в 1.47 раз)
# 100 loops, best of 3: 16.1 msec per loop - 100000 (быстрее в 1.49 раз)
# 100 loops, best of 3: 87.3 msec per loop - 500000 (быстрее в 1.48 раз)


# --------------------------------------------------------------------------------------------------------------

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

# 2.1 Решение вариант 01, через append
def arrindex_append(n):
    array_file = open('array_gen.py')
    array = json.loads(array_file.read())
    array_file.close()
    result = []
    for i in range(len(array)):
        if array[i] % 2 == 0:
            result.append(i)
    return result


# 100 loops, best of 3: 139 usec per loop - 100
# 100 loops, best of 3: 260 usec per loop - 500
# 100 loops, best of 3: 759 usec per loop - 2500
# 100 loops, best of 3: 1.38 msec per loop - 5000
# 100 loops, best of 3: 6.79 msec per loop - 25000
# 100 loops, best of 3: 28 msec per loop - 100000
# 100 loops, best of 3: 148 msec per loop - 500000
# 100 loops, best of 3: 455 msec per loop - 1500000
# 100 loops, best of 3: 3.08 sec per loop - 10000000


# 2.2 Решение вариант 02, через for
def arrindex_for(n):
    array_file = open('array_gen.py')
    array = json.loads(array_file.read())
    array_file.close()
    result = [i for i in range(len(array)) if array[i] % 2 == 0]
    return result


# 100 loops, best of 3: 137 usec per loop - 100
# 100 loops, best of 3: 232 usec per loop - 500 (быстрее в 1.12 раз)
# 100 loops, best of 3: 683 usec per loop - 2500 (быстрее в 1.11 раз)
# 100 loops, best of 3: 1.24 msec per loop - 5000 (быстрее в 1.11 раз)
# 100 loops, best of 3: 5.99 msec per loop - 25000 (быстрее в 1.13 раз)
# 100 loops, best of 3: 24.5 msec per loop - 100000 (быстрее в 1.14 раз)
# 100 loops, best of 3: 131 msec per loop - 500000 (быстрее в 1.13 раз)
# 100 loops, best of 3: 407 msec per loop - 1500000 (быстрее в 1.12 раз)
# 100 loops, best of 3: 2.76 sec per loop - 10000000 (быстрее в 1.11 раз)
