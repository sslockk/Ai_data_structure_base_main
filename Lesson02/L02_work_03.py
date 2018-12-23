num = int(input('Введите натуральное число'))
n = 2
revers_num = 0
while num != 0:
    n = num % 10
    num = num // 10
    revers_num = revers_num * 10 + n

print('Реверс число -', revers_num)
