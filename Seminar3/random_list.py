from random import randint

def fill_list (A, B, len, len_from = 1):
    list = []
    for _ in range(randint(min(len, len_from), max(len, len_from))):
        list.append(randint(A, B))
    return list