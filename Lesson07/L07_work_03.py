# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random

k = 3
SIZE = 2 * k + 1
array = [random.randint(0, 100) for i in range(SIZE)]
print(array)

"""Функция проверки правильности нахождения медианы"""


def proverka_median():
    print('\n Проверка правильности нахождения медианы:')
    array_temp = [1, 2, 3, 4, 5, 6, 7]
    if find_median(array_temp, 3) == 4:
        print('Медиана найдена верно')
    else:
        print('Медиана найдена НЕВЕРНО!!!!')


def find_median(array, k):
    if len(array) == 1:
        assert k == 0
        return array[0]

    pivot = random.choice(array)

    low_array = [x for x in array if x < pivot]
    high_array = [x for x in array if x > pivot]
    pivots = [x for x in array if x == pivot]

    if k < len(low_array):
        return find_median(low_array, k)
    elif k < len(low_array) + len(pivots):
        return pivots[0]
    else:
        return find_median(high_array, k - len(low_array) - len(pivots))


mediana = find_median(array, k)
proverka_median()
print('*' * 40)
print('Медиана равна = ', mediana)
