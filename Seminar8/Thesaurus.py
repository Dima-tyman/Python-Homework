some_str = ["Иван", "Мария", "Петр", "Илья"]
some_str_adv = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

def thesaurus (str):
    list.sort(str)
    temp = []
    dictionary = {str[0][0]:''}
    for i in range(len(str)):
        if i == len(str) - 1:
            temp.append(str[i])
            dictionary[str[i][0]] = list.copy(temp)
            temp.clear()
            break
        if str[i][0] != str[i + 1][0]:
            temp.append(str[i])
            dictionary[str[i][0]] = list.copy(temp)
            temp.clear()
        else:
            temp.append(str[i])
    return dictionary

def reverse_fio (fio_list):
    for i in range(len(fio_list)):
        fio_list[i] = fio_list[i].split()[1] + ' ' + fio_list[i].split()[0]
    return fio_list

def thesaurus_adv (lst):
    reverse_fio(lst)
    dict_first = thesaurus(lst)
    keys = dict_first.keys()
    for key in keys:
        reverse_fio(dict_first[key])
        dict_first[key] = thesaurus(dict_first[key])
    return dict_first

print(thesaurus_adv(some_str_adv))