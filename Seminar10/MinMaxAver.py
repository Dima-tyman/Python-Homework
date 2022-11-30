def Average(some_lst):
        sum = 0
        for i in some_lst:
            sum += i
        return sum / len(some_lst)

class MinStat:

    def __init__(self):
        self.numbers = []
        self.min_num = 'None'

    def add_number(self, num):
        self.numbers.append(int(num))
        if self.min_num == 'None':
            self.min_num = int(num)
        elif int(num) < self.min_num:
            self.min_num = int(num)
        
    def result(self):
        print(f'Текущий минимум: {self.min_num}')

class MaxStat:
    
    def __init__(self):
        self.numbers = []
        self.max_num = 'None'

    def add_number(self, num):
        self.numbers.append(int(num))
        if self.max_num == 'None':
            self.max_num = int(num)
        elif int(num) > self.max_num:
            self.max_num = int(num)
        
    def result(self):
        print(f'Текущий максимум: {self.max_num}')

class AverageStat:
    
    def __init__(self):
        self.numbers = []
        self.aver_num = 'None'

    def add_number(self, num):
        self.numbers.append(int(num))
        if self.aver_num == 'None':
            self.aver_num = int(num)
        else:
            self.aver_num = Average(self.numbers)
        
    def result(self):
        print(f'Текущее среднее: {self.aver_num}')
        
num_min = MinStat()
num_max = MaxStat()
num_aver = AverageStat()
for _ in range(4):
    num_min.add_number(input('Добавить к списку Min '))
    num_min.result()
for _ in range(4):
    num_max.add_number(input('Добавить к списку Max '))
    num_max.result()
for _ in range(4):
    num_aver.add_number(input('Добавить к списку Average '))
    num_aver.result()