import math
from random_list import *

#1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# numbers = fill_list(-10, 10, 5, 15)
# print(numbers)
# sum = 0
# for i in range(1, len(numbers), 2):
#     sum += numbers[i]
# print(sum)


#2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# numbers = fill_list(1, 10, 5, 6)
# print(numbers)
# multi = []
# for i in range(math.ceil(len(numbers) / 2)):
#     multi.append(numbers[i] * numbers[len(numbers) - 1 - i])
# print(multi)


#3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# numbers = [1.1, 1.2, 3.1, 5, 10.01]
# print(numbers)
# max, min = numbers[0] % 1, numbers[0] % 1
# for i in numbers:
#     if i % 1 > max:
#         max = i % 1
#     if i % 1 < min:
#         min = i % 1
# print(max - min)


#4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# print(bin(int(input('Функция '))).split('b')[1])
#
#
# num = int(input('Алгоритм '))
# dec = ''
#
# while num / 2 != 0:
#     dec = str(num % 2) + dec
#     num = math.floor(num / 2)
# print(dec)


#5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# n = int(input())
#
# fibonachi = [None] * (n * 2 + 1)
# fibonachi[n] = 0
# fibonachi[n + 1] = 1
#
# for i in range(n + 2, len(fibonachi)):
#     fibonachi[i] = fibonachi[i - 2] + fibonachi[i - 1]
# for i in range(n - 1, -1, -1):
#     fibonachi[i] = fibonachi[i + 2] - fibonachi[i + 1]
#
# print(fibonachi)


#6. Сгруппировать слова по общим буквам