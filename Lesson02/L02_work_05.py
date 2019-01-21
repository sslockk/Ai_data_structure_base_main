for i in range(32, 127):
    print(f'{i}-{chr(i)}', end=' ')
    if (i - 1) % 10 == 0:
        print()
