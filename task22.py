import random
num_n = int(input('Введите число элементов первого набора целых чисел: '))
num_m = int(input('Введите число элементов второго набора целых чисел: '))

first_collection = [random.randint(0, 10) for i in range(num_n)]
second_collection = [random.randint(0, 10) for i in range(num_m)]

union_set = sorted(
    (set(first_collection)).intersection(set(second_collection)))

print(f'Первый набор\n{first_collection}\nВторой набор\n{second_collection}')
print(f'Итоговый набор\n{union_set}')
