import random
num_n = int(input('Введите число кустов на грядке N: '))
bush_list = [random.randint(0, 10) for i in range(num_n)]
print(f'{bush_list}\n=========================')

max_berry = 0

while num_n != 0:
    if bush_list[0] + bush_list[1] + bush_list[2] > max_berry:
        max_berry = bush_list[0] + bush_list[1] + bush_list[2]
    bush_list.append(bush_list.pop(0))
    num_n -= 1
print(max_berry)
