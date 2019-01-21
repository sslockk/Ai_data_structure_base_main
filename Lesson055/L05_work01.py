# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# # (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# # (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего
# # и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

from collections import namedtuple

n = int(input('Введите кол-во предпиятий'))
all_factory = []

"""Создаем массив из именованых кортежей с именем, прибылью по кварталам и общей прибылью за год """
for i in range(n):
    profit = []
    New_factory = namedtuple('New_factory', 'name quarter_profit year_profit')
    name = input(f'Введите имя предприятия под номером {i + 1}-')
    summ = 0
    for x in range(4):
        profit.append(int(input(f'Введите прибыль у предприятия {i + 1} за квартал №{x + 1} - ')))
        summ += profit[x]
    all_factory.append(New_factory(name, profit, summ))
    print()


"""Находим и выводим средную прибыль за год у всех заводов """
summ = 0
for i in range(n):
    summ += all_factory[i].year_profit

middle_profit_all = int(summ / n)
print('-' * 50)
print('Средняя прибыль за год для всех предприятий = ', middle_profit_all)
print('\n', '-' * 50)

"""Создаем 2 массива, и запишем в них имена предприятий у которых профит больше и меньше среденго значения """
more_middle_profit = []
lower_middle_profit = []
for i in range(n):
    if all_factory[i].year_profit > middle_profit_all:
        more_middle_profit.append(all_factory[i].name)
    else:
        lower_middle_profit.append(all_factory[i].name)

"""Распечатываем по очереди массивы с именами предприятий у которых прибыль больше и меньше средней соответсвенно  """
print('Список предприятий, у которых прибыль ВЫШЕ среднего:')
for x in range(len(more_middle_profit)):
    print(f'{x+1})- {more_middle_profit[x]} ')
print('\n', '-' * 50)

print('Список предприятий, у которых прибыль НИЖЕ среднего:')
for x in range(len(lower_middle_profit)):
    print(f'{x+1}) - {lower_middle_profit[x]} ')
