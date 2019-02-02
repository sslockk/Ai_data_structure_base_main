# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами
# на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).


import random

SIZE = 20
array = [random.randint(-100, 99) for i in range(SIZE)]
print(array)


def booble_sort(array):
    count = 0
    n = 1
    while n < len(array):
        stop_flag = False
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                stop_flag = True
            count += 1

        if stop_flag == False:
            break
        # print(array)
        n += 1
    return count


count = booble_sort(array)
print(array, '\n', 'Количество проходов по массиву =', count)
