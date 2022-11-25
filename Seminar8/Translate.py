number = {'ноль':'zero', 'один':'one', 'два':'two',
          'три':'tree', 'четыре':'four', 'пять':'five',
          'шесть':'six', 'семь':'seven', 'восемь':'eight',
          'девять':'nine', 'десять':'ten'}

def num_translate (sourse):
    return number.get(sourse.lower())

def num_translate_adv (sourse):
    if sourse.istitle():
        return number.get(sourse.lower()).capitalize()
    else:
        return number.get(sourse.lower())

print(num_translate_adv(input('Введите слово для перевода: ')))