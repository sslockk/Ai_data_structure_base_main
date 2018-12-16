# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

x = int(input('Введите номер буквы в алфавите'))
abc_list = 'abcdefghijklmnopqrstuvwxyz'
print('Буква под номером {} это = {}'.format(x, abc_list[x - 1]))
