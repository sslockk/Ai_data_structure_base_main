# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.


import random

SIZE = 10
min_item = -100
max_item = 100
array = [random.randint(min_item, max_item) for _ in range(SIZE)]
print('Массив', array)
i_min = 0
x_min = 0

for i in range(len(array)):
    if x_min > array[i]:
        x_min = array[i]
        i_min = i + 1

print(f'Максимальный отрицательный элемент: {x_min} стоит на  {i_min} месте')
