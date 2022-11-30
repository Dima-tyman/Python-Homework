from random import randint

class Table:
    
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.table = [[None for _ in range(cols)] for _ in range(rows)]

    def random_fill(self):
        self.table = [[randint(10, 50) for _ in range(len(self.table))] for _ in range(len(self.table[0]))]

    def print_table(self):
        for i in self.table:
            print(*i, sep=' ')

    def get_value(self, row, col):
        if row > len(self.table) or col > len(self.table[0]):
            return 'Такой ячейки не существует!'
        else:
            return self.table[row - 1][col - 1]
        
    def set_value(self, row, col, value):
        if row > len(self.table) or col > len(self.table[0]):
            print('Такой ячейки не существует!')
        else:
            self.table[row - 1][col - 1] = value
            
    def n_rows(self):
        return(len(self.table))
        
    def n_cols(self):
        return(len(self.table[0]))

    def delete_row(self, row):
        if row > len(self.table):
            print('Такой строки не существует!')
        else:
            self.table.pop(row - 1)

    def delete_col(self, col):
        if col > len(self.table[0]):
            print('Такой строки не существует!')
        else:
            for i in self.table:
                i.pop(col - 1)

    def add_row(self, row):
        if row > len(self.table) + 1:
            print('Строка записана в конец')
            self.table.insert(len(self.table), [None for _ in range(len(self.table[0]))])
        else:
            self.table.insert(row - 1, [None for _ in range(len(self.table[0]))])

    def add_col(self, col):
        if col > len(self.table[0]) + 1:
            print('Столбец записан в конец')
            for i in self.table:
                i.insert(len(self.table[0]), None)
        else:
            for i in self.table:
                i.insert(col - 1, None)

    
tab = Table(5, 5)
tab.random_fill()
print(tab.get_value(1, 2))
print(tab.get_value(1, 3))
print(tab.get_value(1, 4))
print(tab.n_cols(), tab.n_rows())
tab.delete_col(2)
print(tab.get_value(1, 2))
print(tab.get_value(1, 3))
print(tab.n_cols(), tab.n_rows())
print(tab.get_value(2, 2))
tab.delete_row(1)
print(tab.get_value(1, 2))
print(tab.n_cols(), tab.n_rows())
print(tab.get_value(2, 4))
tab.add_row(2)
print(tab.get_value(2, 4))
print(tab.get_value(3, 4))
tab.add_col(4)
print(tab.get_value(3, 4))
print(tab.get_value(3, 5))
tab.print_table()