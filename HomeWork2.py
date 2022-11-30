# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random
def result(list):
    idx = len(list) - 1
    result = []
    for num in range(round(len(list) / 2)):
        result.append(list[num] * list[idx])
        idx -= 1
    return result
list = [random.randint(1, 10) for _ in range(random.randint(2, 10))]
print(f'Случайный список чисел {list} \nПроизведение пар чисел {result(list)}')