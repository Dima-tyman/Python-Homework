def Sort (data, find):
    sort_data = []
    empty = True
    for row in data:
        if find == row[0]:
            sort_data.append(row)
            empty = False
    if empty:
        return 'Данные не найдены!'
    return sort_data