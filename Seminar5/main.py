import random
import time

#1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'Абв абв пабв абвв вабва вавбв аб бв рнав привет'
# new_text = ' '.join(filter(lambda x: 'абв' not in x, text.split()))
# print(new_text)


#2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# count_sweets = 2021
# count_try = 280
# botsii_name = ['God', 'Fill']
# bots_name = ['Tom', 'Gim']
# players = ['Дима', 'God'] #введите ваши имена или имена ботов
# curent_player = random.randint(0, len(players) - 1)
# sweets = count_sweets
#
# while sweets > 0:
#     if players[curent_player] in botsii_name:
#         if sweets % (count_try + 1) == 0:
#             n = random.randint(1, min(count_try, sweets))
#             print(f'{players[curent_player]} взял {n} (осталось {sweets - n})')
#         else:
#             n = sweets % (count_try + 1)
#             print(f'{players[curent_player]} взял {n} (осталось {sweets - n})')
#             # print(f'{players[curent_player]}: ты неизбежно поиграешь через {int((sweets - n) / (count_try + 1))} ходов!!!')
#     elif players[curent_player] in bots_name:
#         n = random.randint(1, min(count_try, sweets))
#         print(f'{players[curent_player]} взял {n} (осталось {sweets - n})')
#     else:
#         n = int(input(f'Берёт игрок "{players[curent_player]}" (осталось {sweets} конфет): '))
#         while n > count_try or n > sweets or n <= 0:
#             n = int(input(f'Вы взяли неверное кол-во конфет. Осталось {sweets} конфет: '))
#
#     sweets -= n
#
#     if sweets != 0:
#         if curent_player + 1 == len(players):
#             curent_player = 0
#         else:
#             curent_player += 1
#     else:
#         print(f'Победил игрок {players[curent_player]}!')
#     time.sleep(0.1)


#3. Создайте программу для игры в ""Крестики-нолики"".

# sim = ['x', 'o']
# player = ['Вася', 'Петя']
# curent_player = random.randint(0, 1)
# size = 3
# box = [['•' for x in range(size)] for x in range(size)]
# count = 1
# win = False
#
# while count <= size ** 2:
#     for i in range(size):
#         for j in range(size):
#             print(box[i][j] + ' ', end='')
#         print()
#
#     pos = list(map(int, input(f'{player[curent_player]}, введи позицию (строка столбец): ').split()))
#     while pos[0] > size or pos[1] > size or box[pos[0] - 1][pos[1] - 1] != '•':
#         pos = list(map(int, input(f'{player[curent_player]}, введи позицию (строка столбец): ').split()))
#     box[pos[0] - 1][pos[1] - 1] = sim[curent_player]
#
#     if count >= size * len(player) - 1:
#         if box[0][0] == box[0][1] == box[0][2] or\
#            box[1][0] == box[1][1] == box[1][2] or\
#            box[2][0] == box[2][1] == box[2][2] or\
#             \
#            box[0][0] == box[1][0] == box[2][0] or\
#            box[0][1] == box[1][1] == box[2][1] or\
#            box[0][2] == box[1][2] == box[2][2] or\
#             \
#            box[0][0] == box[1][1] == box[2][2] or \
#            box[0][2] == box[1][1] == box[2][0]:
#             win = True
#             break
#
#     if curent_player == 1:
#         curent_player = 0
#     else:
#         curent_player = 1
#
#     count += 1
#
# for i in range(size):
#     for j in range(size):
#         print(box[i][j] + ' ', end='')
#     print()
#
# if win:
#     print('Победил ' + player[curent_player])
# else:
#     print('Ничья')


#4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# string = 'fffffgggdddddffdhhggggggggggggggssd'
# compress = ''
# count = 1
# curent = string[0]
#
# for i in range(1, len(string)):
#     if string[i] == string[i - 1]:
#         count += 1
#     else:
#         compress += str(count) + curent
#         count = 1
#         curent = string[i]
# compress += str(count) + curent
#
# print(string)
# print(compress)
#
# unpack = ''
# multi = ''
# for i in range(len(compress)):
#     if compress[i].isdigit():
#         multi += compress[i]
#     else:
#         unpack += compress[i] * int(multi)
#         multi = ''
# print(unpack)