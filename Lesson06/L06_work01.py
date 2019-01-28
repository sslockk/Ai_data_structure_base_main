# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых
# трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

import random
from collections import Counter
import sys


def max_stolb_element():
    """Программа №1.
    Найти максимальный элемент среди минимальных элементов столбцов матрицы."""
    SIZE = 10
    raw = 4
    min_item = 0
    max_item = 100
    array = []
    array_min = []
    for _ in range(raw):
        array.append([random.randint(min_item, max_item) for _ in range(SIZE)])
    # print('Массив:')
    # [print(array[i]) for i in range(raw)]
    x_max = min_item
    for i in range(SIZE):
        x_min = max_item
        for n in range(raw):
            if x_min > array[n][i]:
                x_min = array[n][i]
        array_min.append(x_min)
    for i in range(len(array_min)):
        if x_max < array_min[i]:
            x_max = array_min[i]
    # print('Максимальный элемент среди минимальных элементов столбцов матрицы:', x_max)
    return [SIZE, array, array_min, i, max_item, min_item, n, raw, x_min, x_max]


def find_chair(a='a', b='d', abc_list='abcefghijklmnopqrstuvwxedewwededwedwewdeyz'):
    """Программа №2.
    Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят
    и сколько между ними находится букв."""
    a_index = abc_list.index(a) + 1
    b_index = abc_list.index(b) + 1
    # print('Буква {} стоит на {} месте алфавита, а буква {} на {} месте'.format(a, a_index, b, b_index))
    # print('Между ними находиться {} букв(а)'.format((b_index - a_index) - 1))
    return [a, a_index, abc_list, b, b_index]


def find_summ_elements():
    """ Программа №3.
    (В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
    Сами минимальный и максимальный элементы в сумму не включать)"""
    SIZE = 20
    min_item = 0
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(SIZE)]
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
    return [SIZE, array, i, i_max, i_min, max_item, min_item, n, summ, x_max, x_min]


def show_size(x):
    """Функция определения объема памяти переменными программы"""
    summ = sys.getsizeof(x)
    # print('\t', f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                summ += show_size(key)
                summ += show_size(value)
        elif not isinstance(x, str):
            for item in x:
                summ += show_size(item)
    return summ


def all_memory(varibles):
    memory_sum = 0
    types = []
    for i in varibles:
        memory_sum += show_size(i)
        types.append(type(i))
    return memory_sum, Counter(types)


print(f'{max_stolb_element.__doc__} \n Объем занимаемой памяти (32-х битная система):\n'
      f'{all_memory(max_stolb_element())[0]} байт \n Типы и кол-во переменных: {all_memory(max_stolb_element())[1]}')
print('*'*50)

print(f'{find_chair.__doc__} \n Объем занимаемой памяти (32-х битная система):\n'
      f'{all_memory(find_chair())[0]} байт \n Типы и кол-во переменных: {all_memory(find_chair())[1]}')
print('*'*50)

print(f'{find_summ_elements.__doc__} \n Объем занимаемой памяти (32-х битная система):\n'
      f'{all_memory(find_summ_elements())[0]} байт \n Типы и кол-во переменных: {all_memory(find_summ_elements())[1]}')

"""Программа №2 эффективннее использует память. Выражаеться в меньшем кол-ве переменных."""



