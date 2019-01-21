# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

SIZE = 10
raw = 4
min_item = 0
max_item = 100
array = []
array_min = []
for _ in range(raw):
    array.append([random.randint(min_item, max_item) for _ in range(SIZE)])

print('Массив:')
[print(array[i]) for i in range(raw)]
x_max = 0

for i in range(SIZE):
    x_min = max_item
    for n in range(raw):
        if x_min > array[n][i]:
            x_min = array[n][i]
    array_min.append(x_min)

print('Массив из минимальных элементов столбцов', array_min)

for i in range(len(array_min)):
    if x_max < array_min[i]:
        x_max = array_min[i]

print('Максимальный элемент среди минимальных элементов столбцов матрицы:', x_max)
