#1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# from curses.ascii import isdigit

# n = input()
# sum_num = 0

# for i in range(len(n)):
#     if n[i].isdigit():
#         sum_num += int(n[i])

# print(sum_num)    ---   Выдаёт ошибку "ModuleNotFoundError: No module named '_curses'"


# n = input()
# sum_num = 0

# for i in range(len(n)):
#     if n[i] == ',' or n[i] == '.':
#         continue
#     sum_num += int(n[i])

# print(sum_num)


#2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# N = int(input())
# num = 1

# for i in range(1, N):
#     num *= i
#     print(num, end=', ')
# print(num * N)


#3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

# n = int(input())
# sum = 0
#
# for i in range(1, n):
#     print(i, ':', round((1 + 1 / i) ** i, 2), end=', ')
#     sum += (1 + 1 / i) ** i
# print(n, ':', round((1 + 1 / n) ** n, 2))
# sum += (1 + 1 / n) ** n
#
# print(round(sum, 2))


#4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#   Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

# import random
#
# N = int(input())
#
# numbers = [-N]
# for i in range(1, N - 1):
#     numbers.append(random.randint(-N, N))
# numbers.append(N)
# print(numbers)
#
# with open('x.txt', 'r') as file:
#     content = []
#     for line in file:
#         content.append(int(line.replace('\n', '')))
# print(content)
#
# multi = 1
# for i in content:
#     multi *= numbers[i]
# print(multi)


#5. Реализуйте алгоритм перемешивания списка.

# import random

# list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# ran_list = []
# print(list)

# Вариант 1
# for i in range(len(list)):
#     ran = random.randint(0, len(list) - 1)
#     temp = list[ran]
#     list[ran] = list[i]
#     list[i] = temp
# print(list)

# Вариант 2
# for i in range(len(list)):
#     temp = random.choice(list)
#     ran_list.append(temp)
#     list.remove(temp)
# print(ran_list)

# Вариант 3
# random.shuffle(list)
# print(list)


#6. Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2] Надо вернуть их пересечение [1, 2, 2, 3] (порядок не важен)

# arr1 = [1, 2, 3, 2, 0]
# arr2 = [5, 1, 2, 7, 3, 2]
# arr_inner = []
#
# for i in arr1:
#     if i in arr2:
#         arr_inner.append(i)
#         arr2.remove(i)
#
# print(arr_inner)
