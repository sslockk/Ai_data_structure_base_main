# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами
# на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
array = [round(random.uniform(0, 50), 3) for i in range(SIZE)]
print(array)


def merge_sort(array):
    def merge(left, right):
        array_temp = []
        while left and right:
            if left[0] < right[0]:
                array_temp.append(left.pop(0))
            else:
                array_temp.append(right.pop(0))
        if left:
            array_temp.extend(left)
        if right:
            array_temp.extend(right)
        return array_temp

    length = len(array)
    if length >= 2:
        mid = int(length / 2)
        array = merge(merge_sort(array[:mid]), merge_sort(array[mid:]))
    return array


a = merge_sort(array)
print(a)
