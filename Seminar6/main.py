from random import randint

#1. Обработать список

# li = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
#
# i = 0
# while i < len(li):
#     if li[i].isdigit():
#         if len(li[i]) == 1:
#             li[i] = '0' + li[i]
#         li.insert(i+1, " '")
#         li.insert(i, "' ")
#         i += 2
#     elif li[i][1:].isdigit():
#         if len(li[i]) == 2:
#             li[i] = li[i][:1] + '0' + li[i][1:]
#         li.insert(i+1, " '")
#         li.insert(i, "' ")
#         i += 2
#     i += 1
#
# text = ' '.join(li).replace("'  ", "'").replace("  '", "'")
# print(text)


#2. Искажённые данные

# li = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
# # for i in li:
# #     print(f'Привет, {i.split()[-1].title()}!')
# # print()
# for i in range(len(li)):
#     li[i] = ' '.join(li[i].split()[:-1]) + ' ' + li[i].split()[-1].title()
#     print(f'Привет, {li[i].split()[-1]}!')
# print(li)


#3. Список цен

# price = [randint(1, 10000)/100 for _ in range(10)]
# print(price)
#
# def PrintPrice (li, end = -1):
#     ind = 0
#     for num in li:
#         if len(str(num).split('.')[1]) == 1:
#             print(f'{str(num).split(".")[0]} руб 0{str(num).split(".")[1]} коп', end=', ')
#         else:
#             print(f'{str(num).split(".")[0]} руб {str(num).split(".")[1]} коп', end=', ')
#         ind += 1
#         if ind == end: break
#
# PrintPrice(price)
# print()
#
# price.sort()
# PrintPrice(price)
# print()
#
# price.reverse()
# PrintPrice(price)
# print()
#
# PrintPrice(price, 5)
# print()
#
# print(price)