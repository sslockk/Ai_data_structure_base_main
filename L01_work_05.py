# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

a = input('Введите первую букву')
b = input('Введите конечную букву')
abc_list = 'abcdefghijklmnopqrstuvwxyz'
a_index = abc_list.index(a)+1
b_index = abc_list.index(b)+1
print('Буква {} стоит на {} месте алфавита, а буква {} на {} месте'.format(a, a_index, b, b_index))
print('Между ними находиться {} букв(а)'.format((b_index - a_index) - 1))
