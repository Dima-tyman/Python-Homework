import csv

def ImportData (some_str):
    str = some_str.split()
    with open('phone_dir.csv', 'a', encoding='UTF-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(str)

def ExportData ():
    with open('phone_dir.csv', 'r', encoding='UTF-8', newline='') as f:
        return list(csv.reader(f))