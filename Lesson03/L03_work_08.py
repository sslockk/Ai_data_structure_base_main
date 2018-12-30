# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму
# введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

array = []

for n in range(1, 5):
    array_raw = []
    summ = 0
    for i in range(4):
        num = int(input(f'Введите {i} элементы строки {n}:'))
        array_raw.append(num)
        summ += num
    array_raw.append(summ)
    array.append(array_raw)

print('Матрица 5x4:\n', array)
