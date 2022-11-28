class SeaMap:
    convert_char = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    size = 10

    def new_desk(self):
        self.sea_grid = [['.' for _ in range(self.size + 2)] for _ in range(self.size + 2)]
        for i in range(1, self.size + 1):
            self.sea_grid[0][i] = self.convert_char[i]
            self.sea_grid[i][0] = i
        self.sea_grid[10][0] = 0
        self.sea_grid[0][0] = ' '


    def display_grid(self):
        for i in range(len(self.sea_grid) - 1):
            for j in range(len(self.sea_grid[0]) - 1):
                print(self.sea_grid[i][j], end=' ')
            print()

    def shoot(self, cell, res):
        column = self.convert_char.index(cell[0].upper())
        row = int(cell[1:3])
        if self.sea_grid[row][column] != '.':
            print('Сюда уже стреляли или тут нет корабля!')
        elif res == 'miss' or res == 'm' or res == '1':
            self.sea_grid[row][column] = '*'
        elif (res == 'silk' or res == 's' or res == '2' or res == 'hit' or res == 'h' or res == '3') and \
        (self.sea_grid[row + 1][column + 1] == 'X' or self.sea_grid[row + 1][column - 1] == 'X' \
         or self.sea_grid[row - 1][column + 1] == 'X' or self.sea_grid[row - 1][column - 1] == 'X'):
            print('Тут не может быть корабля!')
        elif res == 'silk' or res == 's' or res == '2':
            self.sea_grid[row][column] = 'X'
        elif res == 'hit' or res == 'h' or res == '3':
            self.sea_grid[row][column] = 'X'
            self.ship_kill(row, column)
        self.display_grid()

    def ship_kill(self, x, y):
        self.sea_grid[x][y] = 'Х'
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0: continue
                if self.sea_grid[x + i][y + j] == '.':
                    self.sea_grid[x + i][y + j] = '*'
                elif self.sea_grid[x + i][y + j] == 'X':
                    self.ship_kill(x + i, y + j)

print('miss/m/1 - мимо, silk/s/2 - попал, hit/h/3 - убил')
sea_map = SeaMap()
sea_map.new_desk()
sea_map.display_grid()
while True:
    command = input('Ячейка - статус: ').split()
    if len(command) != 2:
        break
    sea_map.shoot(command[0], command[1])