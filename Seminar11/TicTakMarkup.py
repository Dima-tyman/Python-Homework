from telebot import types

player_one = 'Игрок 1'
player_two = 'Игрок 2'
player_one_id = None
player_two_id = None
sells = ['11', '12', '13', '21', '22', '23', '31', '32', '33']

def up_home():
    global player_one, player_two
    home_page = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    player1 = types.KeyboardButton(player_one)
    player2 = types.KeyboardButton(player_two)
    one_player = types.KeyboardButton('Одиночная игра')
    swith_player = types.KeyboardButton('Поменяться местами')
    game_start = types.KeyboardButton('Начать игру!')
    back_buttom = types.KeyboardButton('EXIT')
    home_page.add(player1, player2, one_player, swith_player, game_start, back_buttom)
    return home_page

game_page = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
sell11 = types.KeyboardButton('11')
sell12 = types.KeyboardButton('12')
sell13 = types.KeyboardButton('13')
sell21 = types.KeyboardButton('21')
sell22 = types.KeyboardButton('22')
sell23 = types.KeyboardButton('23')
sell31 = types.KeyboardButton('31')
sell32 = types.KeyboardButton('32')
sell33 = types.KeyboardButton('33')
game_end = types.KeyboardButton('Закончить игру')
game_page.add(sell11, sell12, sell13, sell21, sell22, sell23, sell31, sell32, sell33, game_end)


def init_players(name, id, player):
    global player_one
    global player_two
    global player_one_id
    global player_two_id
    if player == 1:
        player_one = name
        player_one_id = id
    elif player == 2:
        player_two = name
        player_two_id = id

def swith():
    global player_one
    global player_two
    global player_one_id
    global player_two_id
    temp = player_one
    player_one = player_two
    player_two = temp
    temp = player_one_id
    player_one_id = player_two_id
    player_two_id = temp