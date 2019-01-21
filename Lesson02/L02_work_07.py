n = int(input('Введите натуральное число'))
sum = 0
for i in range(1, n + 1):
    sum += i
sum2 = int(n * (n + 1) / 2)
print('Сумма чисел по формуле 1+2+..n =', sum)
print('Сумма чисел по формуле n(n+1)/2 = ', sum2)
