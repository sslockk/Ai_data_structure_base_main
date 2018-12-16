# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input('Введите год'))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('Год {} високосный'.format(year))
        else:
            print('Год {}  НЕ високосный'.format(year))
    else:
        print('Год {} високосный'.format(year))

else:
    print('Год {} НЕ високосный'.format(year))
