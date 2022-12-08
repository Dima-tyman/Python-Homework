class TicTacToeBoard:

     simbol = ['O', 'X']
     split = '--'

     def new_game(self, pl1, pl2, name1, name2):
          self.players = [pl1, pl2]
          self.players_name = [name1, name2]
          self.curent_players = 0
          self.board = [[self.split for _ in range(3)] for _ in range(3)]
          self.winner = ' '
          self.step = 1

     def get_field (self):
          text = ''
          for row in self.board:
               for columns in row:
                    print(columns, end=' ')
                    text += columns
               text += '\n'
               print()
          return text


     def check_field(self):
          if self.board[0][0] == self.board[0][1] == self.board[0][2] != self.split or \
             self.board[1][0] == self.board[1][1] == self.board[1][2] != self.split or \
             self.board[2][0] == self.board[2][1] == self.board[2][2] != self.split or \
             self.board[0][0] == self.board[1][0] == self.board[2][0] != self.split or \
             self.board[0][1] == self.board[1][1] == self.board[2][1] != self.split or \
             self.board[0][2] == self.board[1][2] == self.board[2][2] != self.split or \
             self.board[0][0] == self.board[1][1] == self.board[2][2] != self.split or \
             self.board[0][2] == self.board[1][1] == self.board[2][0] != self.split:
               self.winner = self.players[self.curent_players]
               return f'Победил игрок {self.players_name[self.curent_players]}!'
          elif self.step == len(self.board) * len(self.board[1]):
               self.winner = 'non'
               return 'Ничья!'
          else:
               return 'Игра продолжается!'

     def make_move(self, sell):
          row = int(sell[0])
          column = int(sell[1])
          if self.winner != ' ' or self.step > len(self.board) * len(self.board[1]):
               return 'Игра уже завершена! Начните новую игру.'
          elif row > len(self.board) or column > len(self.board[1]):
               return 'Такой ячейки нет!'
          elif self.board[row - 1][column - 1] != self.split:
               return 'Эта ячейка уже занята!'
          else:
               self.board[row - 1][column - 1] = self.simbol[self.curent_players]
               if self.check_field() == 'Игра продолжается!':
                    if self.curent_players == 0:
                         self.curent_players = 1
                    else:
                         self.curent_players = 0
                    self.step += 1
                    return self.get_field()
               else:
                    return self.get_field() + self.check_field()