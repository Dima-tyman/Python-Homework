import random
from random import randint

#1. Вычислить число c заданной точностью d

# print(round(float(input('Введите число: ')), len(input('Введите точность: ').split('.')[1])))


#2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# n = int(input())
# list_multiplier = []
# for i in range(2, n):
#     simple = True
#     if n % i == 0:
#         for j in range(2, i):
#             if i % j == 0:
#                 simple = False
#                 break
#         if simple:
#             list_multiplier.append(i)
# print(list_multiplier)


#3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list1 = []
# nonrep_list = []
# for _ in range(10):
#     list1.append(randint(0, 10))
# list1.sort()
# print(list1)
# print(list(set(list1)))
# for i in list1:
#     if i not in nonrep_list:
#         nonrep_list.append(i)
# print(nonrep_list)


#4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# k = int(input())
# with open('file2.txt', 'w', encoding='UTF-8') as f:
#     polynominal = str(randint(1, 100))
#     for i in range(1, k + 1):
#         if randint(0, 1) == 0:
#             sig = '+'
#         else:
#             sig = '-'
#         if i == 1:
#             polynominal = str(randint(1, 100)) + 'x' + sig + polynominal
#         else:
#             polynominal = str(randint(1, 100)) + 'x(' + str(i) + ')' + sig + polynominal
#     f.write(polynominal)


#5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.


with open('file1.txt', 'r', encoding='UTF-8') as A:
    a = A.readline().replace('-', '.-')\
                    .replace('+', '.')\
                    .replace('(', '')\
                    .replace(')', '')\
                    .split('.')
with open('file2.txt', 'r', encoding='UTF-8') as B:
    b = B.readline().replace('-', '.-')\
                    .replace('+', '.')\
                    .replace('(', '')\
                    .replace(')', '')\
                    .split('.')

for i in range(len(a)):
    a[i] = int(a[i].split('x')[0])
for i in range(len(b)):
    b[i] = int(b[i].split('x')[0])

if len(a) > len(b):
    for i in range(len(a) - len(b)):
        b.insert(0, 0)
else:
    for i in range(len(b) - len(a)):
        a.insert(0, 0)

c = []
for i in range(len(a)):
    if a[i] + b[i] >= 0 and i != 0:
        c.append('+' + str(a[i] + b[i]))
    else:
        c.append(str(a[i] + b[i]))

with open('sum.txt', 'w', encoding='UTF-8') as f:
    polynominal = ''
    for i in range(1, len(c)):
        if i == 1:
            polynominal = str(c[-(i + 1)]) + 'x' + polynominal
        else:
            polynominal = str(c[-(i + 1)]) + 'x(' + str(i) + ')' + polynominal
    polynominal += c[-1]
    f.write(polynominal)