# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

import random

SIZE = 10
min_item = 2
max_item = 99
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print('Массив', array)

for n in range(2, 10):
    array_temp = []
    for i in range(len(array)):
        if array[i] % n == 0:
            array_temp.append(array[i])
    print(f'Числа {array_temp} из массива кратны {n}')
