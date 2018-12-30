# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой
# (оба являться минимальными), так и различаться.

import random

SIZE = 10
min_item = 0
max_item = 100
array = array_temp = [random.randint(min_item, max_item) for _ in range(SIZE)]
print('Массив\n', array)

for n in range(1, 3):
    x_min = array[0]
    i_min = 0
    for i in range(len(array)):
        if x_min > array[i]:
            x_min = array[i]
            i_min = i
    print(f'{n}-ый минимальный эелементы {array_temp.pop(i_min)} ')

