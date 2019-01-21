x = int(input('Введите сколько натуральных чисел будет введено'))
sum_max = 0
num_max = 0
for i in range(x):
    num = int(input(f'Введите натуральное число номер {i + 1} -'))
    sum = 0
    num_temp = num
    while num != 0:
        n = num % 10
        num = num // 10
        sum += n
    if sum > sum_max:
        sum_max = sum
        num_max = num_temp
print(f'Число с наибольшей по сумме цифр - {num_max} и сумма его цифр - {sum_max}')
