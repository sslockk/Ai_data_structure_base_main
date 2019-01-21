# 2. Написать два алгоритма нахождения i-го по счёту простого числа.

# 2.1 Вариант 01( без решета Эратосфена)


def simple_for(n):
    result = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in result:
            if j * j - 1 > i:
                result.append(i)
                break
            if i % j == 0:
                break
        else:
            result.append(i)
    return result[-1]

# 100 loops, best of 3: 2.16 usec per loop - 10
# 100 loops, best of 3: 4.74 usec per loop - 20
# 100 loops, best of 3: 26.2 usec per loop - 100
# 100 loops, best of 3: 179 usec per loop - 500
# 100 loops, best of 3: 1.33 msec per loop - 2500
# 100 loops, best of 3: 2.99 msec per loop - 5000
# 100 loops, best of 3: 22.3 msec per loop - 25000
# 100 loops, best of 3: 149 msec per loop - 100000
# 100 loops, best of 3: 1.39 sec per loop - 500000
# 50 loops, best of 3:  3.19 sec per loop - 1000000

# --------------------------------------------------------------------------------------------------------------

# 2.2 Вариант 02(решето Эратосфена)


def sipmle_eratosfen(n):
    a = [i for i in range(n + 1)]
    a[1] = 0
    result = []
    i = 2
    while i <= n:
        if a[i] != 0:
            result.append(a[i])
            for j in range(i, n + 1, i):
                a[j] = 0
        i += 1
    return result[-1]

# 100 loops, best of 3:  4.87  usec per loop - 10
# 100 loops, best of 3:  8.86 usec per loop - 20
# 100 loops, best of 3:  33.9 usec per loop - 100
# 100 loops, best of 3:  185 usec per loop - 500 (почти одинаковая скорость)
# 100 loops, best of 3:  956 usec per loop - 2500 (быстрее в 1.39 раз)
# 100 loops, best of 3:  1.91 msec per loop - 5000 (быстрее в 1.56 раз)
# 100 loops, best of 3:  9.82 msec per loop - 25000 (быстрее в 2.3 раз)
# 100 loops, best of 3:  43.1 msec per loop - 100000 (быстрее в 3.5 раз)
# 100 loops, best of 3: 273 msec per loop - 500000 (быстрее в 5 раз)
# 50 loops, best of 3: 521 msec per loop - 1000000 (быстрее в 6.1 раз)
