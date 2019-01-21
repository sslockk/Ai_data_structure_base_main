import random

num = random.randint(0, 100)
for i in range(10):
    x = int(input(f'Попытка № {i + 1}. Введите число '))
    if x != num:
        print('Вы НЕ угадали число')
        if x < num:
            print(f'Верное число больше {x}')
        else:
            print(f'Верное число меньше {x}')
    else:
        print(f'!!!!!Вы угадали число {num}')
        exit()
print(f'Вы НЕ угадали число. Это было {num}')
