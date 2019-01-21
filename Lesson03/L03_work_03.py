# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
min_item = 0
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print('Массив\n', array)
x_max = 0
i_max = 0
x_min = array[0]
i_min = 0

for i in range(len(array)):
    if x_min > array[i]:
        x_min = array[i]
        i_min = i
    if x_max < array[i]:
        x_max = array[i]
        i_max = i

print(f'Максимальное число: {x_max} стоит на {i_max + 1} месте, минимальное число: {x_min} стоит на {i_min + 1} месте')
array[i_min], array[i_max] = array[i_max], array[i_min]
print('Новый массив:\n', array)
