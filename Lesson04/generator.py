import random
import sys

if __name__ == '__main__':
    def array_gen(n):
        SIZE = int(n)
        min_item = 0
        max_item = 100
        array = [random.randint(min_item, max_item) for _ in range(SIZE)]
        # print('Массив\n', array)
        file_gen = open('array_gen.py', "w")
        file_gen.write(str(array))
        file_gen.close
        return array
    array_gen(sys.argv[1])


