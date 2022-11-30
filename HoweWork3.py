#Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов

import random

n = int(input("Задайте длину списка вещественных чисел: "))
list = list(random.uniform(0.1, 10.99) for i in range(n))
print("Список из вещественных чисел:")
for i in list:
    print('%.2f' % i)


min = 1
max = 0
for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i) 
dif = max - min 
print(f'разница между макс и мин значением дробной части {round(dif, 2)}')