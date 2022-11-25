colunms_name = ['Фамилия', 'Имя', 'Отчество', 'Телефон' ,'Описание']

def Mode ():
    mod = int(input('Выберите режим работы: EXPORT - 1, IMPORT - 2 - '))
    while mod != 1 and mod != 2:
        mod = int(input('Такого режима нет! Выберите: EXPORT - 1, IMPORT - 2 - '))
    return mod

def InputData ():
    some_str = input(f"Введите данные в формате {' '.join(colunms_name)}: ")
    return some_str

def InputFinder ():
    finder = input('Введите искомое значение: ')
    return finder

def PrintData (data):
    print(', '.join(colunms_name[1:]))
    for row in data:
        print(', '.join(row[1:]))

def PrintNotFind ():
    print('Данные не найдены!')