num = int(input('Введите натуральное число'))
i = 0
v = 0
n = 2
chet_num = ''
non_chet_num = ''
while num != 0:
    n = num % 10
    num = num // 10
    if n % 2:
        # if n !=0:
        i += 1
        non_chet_num += f'{n}'

    else:
        if n != 0:
            v += 1
            chet_num += f'{n}'

print(f'Количество нечетных цифр ={i}. Это - {non_chet_num}')
print(f'Количество четных цифр ={v}. Это - {chet_num}')
