n = input('Введите знак операции(Если 0 - то выход из программы)')
while n != str(0):
    x = float(input('Введите первое число'))
    y = float(input('Введите второе число'))
    while y == 0:
        print('На ноль делить нельзя')
        y = float(input('Введите второе число'))
    if n == '+':
        print(x + y)

    elif n == '-':
        print(x - y)
    elif n == '*':
        print(x * y)
    elif n == '/':
        print(x / y)
    else:
        print('Введен неверный знак операции')

    n = input('Введите знак операции(Если 0 - то выход из программы)')
