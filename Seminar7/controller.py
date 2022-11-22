import view
import log
import model

def Import ():
    print('Наберите q для выхода из ввода, del для удаления последнего ввода')
    while True:
        str = view.InputData()
        if str == 'q':
            break
        elif len(list(str.split())) != 4:
            print('Вы ввели неполные данные, повторите ввод')
        else:
            log.ImportData(str)

def Export ():
    find = view.InputFinder()
    data = log.ExportData()
    sort_data = model.Sort(data, find)
    if type(sort_data) == 'str':
        view.PrintNotFind()
    else:
        view.PrintData(sort_data)