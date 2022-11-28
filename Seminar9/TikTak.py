class TicTacToeBoard:

     players = ['O', 'X']

     def new_game(self):
          self.curent_players = 0
          self.board = [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]
          self.winner = ' '
          self.step = 1

     def get_field (self):
          for row in self.board:
               for columns in row:
                    print(columns, end=' ')
               print()

     def check_field(self):
          if self.board[0][0] == self.board[0][1] == self.board[0][2] != '.' or \
             self.board[1][0] == self.board[1][1] == self.board[1][2] != '.' or \
             self.board[2][0] == self.board[2][1] == self.board[2][2] != '.' or \
             self.board[0][0] == self.board[1][0] == self.board[2][0] != '.' or \
             self.board[0][1] == self.board[1][1] == self.board[2][1] != '.' or \
             self.board[0][2] == self.board[1][2] == self.board[2][2] != '.' or \
             self.board[0][0] == self.board[1][1] == self.board[2][2] != '.' or \
             self.board[0][2] == self.board[1][1] == self.board[2][0] != '.':
               self.winner = self.players[self.curent_players]
               print(f'Победил игрок {self.players[self.curent_players]}!')
          elif self.step == len(self.board) * len(self.board[1]):
               print('Ничья!')
          else:
               print('Игра продолжается!')

     def make_move(self, row, column):
          if self.winner != ' ' or self.step > len(self.board) * len(self.board[1]):
               print('Игра уже завершена! Начните новую игру.')
          elif row > len(self.board) or column > len(self.board[1]):
               print('Такой ячейки нет!')
          elif self.board[row - 1][column - 1] != '.':
               print('Эта ячейка уже занята!')
          else:
               self.board[row - 1][column - 1] = self.players[self.curent_players]
               self.check_field()
               if self.curent_players == 0:
                    self.curent_players = 1
               else:
                    self.curent_players = 0
               self.step += 1


board = TicTacToeBoard()
board.new_game()
board.get_field()
board.make_move(1, 1)
board.get_field()
board.make_move(2, 1)
board.get_field()
board.make_move(2, 1)
board.make_move(2, 4)
board.make_move(1, 3)
board.make_move(1, 2)
board.make_move(2, 2)
board.make_move(3, 3)
board.make_move(3, 2)
board.make_move(3, 2)
board.get_field()
board.make_move(3, 1)
board.get_field()
board.make_move(2, 3)
board.get_field()
board.make_move(2, 3)