# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется
# как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера:
# [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].


from collections import deque
from collections import Counter

numbers = []
for i in range(2):
    numbers.append(deque(input(f'Введите 16-тиричное число номер {i + 1} -')))


def convert_to_16(massive):
    massive_out = []
    for i in range(len(massive)):
        try:
            massive_out.append(int(massive[i]))
        except ValueError:
            if massive[i] == 'A':
                massive_out.append(10)
            elif massive[i] == 'B':
                massive_out.append(11)
            elif massive[i] == 'C':
                massive_out.append(12)
            elif massive[i] == 'D':
                massive_out.append(13)
            elif massive[i] == 'E':
                massive_out.append(14)
            elif massive[i] == 'F':
                massive_out.append(15)
            else:
                print('Неправильно введено число')
                break
    return massive_out


def convert_to_10(massive):
    for i in range(len(massive)):
        if massive[i] > 9:
            if massive[i] == 10:
                massive[i] = 'A'
            elif massive[i] == 11:
                massive[i] = 'B'
            elif massive[i] == 12:
                massive[i] = 'C'
            elif massive[i] == 13:
                massive[i] = 'D'
            elif massive[i] == 14:
                massive[i] = 'E'
            elif massive[i] == 15:
                massive[i] = 'F'
    # return list(reversed(massive))
    return massive


if len(numbers[1]) > len(numbers[0]):
    numbers[0], numbers[1] = numbers[1], numbers[0]
zero = deque(['0'] * (len(numbers[0]) - len(numbers[1])))
numbers[1].extendleft(zero)
numbers_ten = [convert_to_16(numbers[i]) for i in range(2)]


def summ_2(numbers_ten1, numbers_ten2):
    """Сложение чисел"""
    if len(numbers_ten1) > len(numbers_ten2):
        numbers_ten2.insert(0, 0)
    elif len(numbers_ten2) > len(numbers_ten1):
        numbers_ten1.insert(0, 0)
    summ = []
    n = 0
    for i in range(len(numbers_ten1) - 1, -1, -1):
        if (numbers_ten1[i] + numbers_ten2[i] + n) > 15:
            summ.append((numbers_ten1[i] + numbers_ten2[i] + n) - 16)
            n = 1
        else:
            summ.append(numbers_ten1[i] + numbers_ten2[i] + n)
            n = 0
    if n == 1:
        summ.append(n)
    return summ


print('СЛОЖЕНИЕ, сумма =', list(reversed(convert_to_10(summ_2(numbers_ten[0], numbers_ten[1])))))

"""Умножение чисел"""
mult = []
t = 0
for i in range(len(numbers_ten[0]) - 1, -1, -1):
    mult_summ = [0]
    n = 0
    transfer = 0
    for x in range(len(numbers[0]) - 1, -1, -1):
        tmp = numbers_ten[0][x] * numbers_ten[1][i] + mult_summ[n]
        if tmp > 15:
            transfer = tmp // 16
            mult_summ[-1] = tmp - transfer * 16
        else:
            mult_summ[n] = tmp
            transfer = 0
        mult_summ.append(transfer)
        n += 1
    for i in range(t):
        mult_summ.insert(0, 0)
    if len(mult_summ) != Counter(mult_summ)[0]:
        mult.append(list(reversed(mult_summ)))
    n += 1
    t += 1

temp = mult[0]
for i in range(len(mult) - 1):
    temp = list(reversed(summ_2(temp, mult[i + 1])))

print('УМНОЖЕНИЕ чисел =', convert_to_10(temp))
