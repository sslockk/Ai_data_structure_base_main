# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив
# со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6
# (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

import random

SIZE = 10
min_item = 2
max_item = 99
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print('Массив', array)
array_chet = []

for i in range(len(array)):
    if array[i] % 2 == 0:
        array_chet.append(i)

print('Массив с индексами четных цифр первого массива(индексация начинаеться с 0) - ', array_chet)