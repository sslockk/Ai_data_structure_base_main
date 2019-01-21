# 4. Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 10
min_item = 0
max_item = 10
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print('Массив', array)
max_count = 0
x_max = 0

for i in range(len(array)):
    if array.count(array[i]) > max_count:
        max_count = array.count(array[i])
        x_max = array[i]

print(f'Чаще всего встречаеться {x_max} - {max_count} раз')
