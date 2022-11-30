#Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка с нечетными индексами


import random

n = int(input("Задайте длину списка чисел: "))
list = list(random.randint(0, 10) for i in range(n))
print("Список из нескольких чисел:")
print(list)

sum = 0
print("На нечетных позициях элементы: ")
for i in range(1, len(list), 2):
    print(list[i], end=', ')
    sum += list[i]

print(f'\nСумма элементов на нечетных позициях {sum}')