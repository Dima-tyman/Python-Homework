import telebot
from telebot import types
import TicTakMarkup
import TikTak

with open('token.txt', 'r') as t:
    token = t.read()
bot = telebot.TeleBot(token)

with open('chat.txt', 'r') as f:
    chat_id = int(f.read())

commands_list = ['/help', '/start', '/id']

game = TikTak.TicTacToeBoard()

game_list = ['/TicTac']
curent_game = None
game_start = False
curent_player = 0


@bot.message_handler(commands=['init'])
def help_info(message):
    global chat_id
    bot.send_message(chat_id, 'Я больше не с вами(. Позови меня /init')
    with open('chat.txt', 'w') as f:
        f.write(str(message.chat.id))
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Привет!\nНабери /help для вызова комманд.\nНабери /start для выбора игр.')

@bot.message_handler(commands=['help'])
def help_info(message):
    bot.send_message(chat_id, ' '.join(commands_list))

@bot.message_handler(commands=['id'])
def help_info(message):
    bot.send_message(chat_id, message.chat.id)


@bot.message_handler(commands=['start'])
def start_show_buttom(message):
    change_game = types.ReplyKeyboardMarkup(resize_keyboard=True)
    game1 = types.KeyboardButton(game_list[0])
    change_game.add(game1)
    bot.send_message(chat_id, 'Выбери игру!', reply_markup=change_game)


@bot.message_handler(commands=[game_list[0][1:]]) #TicTac
def start_game_TicTac(message):
    global curent_game
    curent_game = 0
    bot.send_message(chat_id, 'Добро пожаловать в игру TicTac!', reply_markup=TicTakMarkup.up_home())


@bot.message_handler(content_types=['text'])
def message_reply(message):
    global curent_game
    global curent_player
    global game_start
    if message.text == 'EXIT' and curent_game != None:
        curent_game = None
        curent_player = 0
        start_show_buttom(message)
    elif curent_game != None:
        if curent_game == 0:
            if message.text == TicTakMarkup.player_one:
                TicTakMarkup.init_players(message.from_user.first_name, message.from_user.id, 1)
                bot.send_message(chat_id, 'Смена игрока 1', reply_markup=TicTakMarkup.up_home())
                print(TicTakMarkup.player_one, TicTakMarkup.player_one_id)
            elif message.text == TicTakMarkup.player_two:
                TicTakMarkup.init_players(message.from_user.first_name, message.from_user.id, 2)
                bot.send_message(chat_id, 'Смена игрока 2', reply_markup=TicTakMarkup.up_home())
                print(TicTakMarkup.player_two, TicTakMarkup.player_two_id)
            elif message.text == 'Одиночная игра':
                TicTakMarkup.init_players(message.from_user.first_name, message.from_user.id, 1)
                TicTakMarkup.init_players(message.from_user.first_name, message.from_user.id, 2)
                bot.send_message(chat_id, f'Привет {message.from_user.first_name}')
            elif message.text == 'Поменяться местами':
                TicTakMarkup.swith()
                bot.send_message(chat_id, 'Игроки сменены', reply_markup=TicTakMarkup.up_home())
            elif message.text == 'Начать игру!':
                if TicTakMarkup.player_one_id == None:
                    bot.send_message(chat_id, 'Игрок 1 не выбран!')
                elif TicTakMarkup.player_two_id == None:
                    bot.send_message(chat_id, 'Игрок 2 не выбран!')
                elif TicTakMarkup.player_one_id != None and TicTakMarkup.player_two_id != None:
                    bot.send_message(chat_id, 'Начнём игру!', reply_markup=TicTakMarkup.game_page)
                    game_start = True
                    game.new_game(TicTakMarkup.player_one_id, TicTakMarkup.player_two_id, TicTakMarkup.player_one, TicTakMarkup.player_two)
                    bot.send_message(chat_id, f'Ходит {TicTakMarkup.player_one} (O)')
            elif game_start:
                if message.text == 'Закончить игру':
                    bot.send_message(chat_id, 'Игра остановлена', reply_markup=TicTakMarkup.up_home())
                    game_start = False
                elif message.text in TicTakMarkup.sells and message.from_user.id == game.players[game.curent_players]:   #основной ход
                    bot.send_message(chat_id, game.make_move(message.text))
                    if game.winner != ' ':
                        bot.send_message(chat_id, 'Игра закончена', reply_markup=TicTakMarkup.up_home())
                    else:
                        bot.send_message(chat_id, f'Ходит {game.players_name[game.curent_players]} ({game.simbol[game.curent_players]})')
                elif message.text in TicTakMarkup.sells and message.from_user.id not in game.players:
                    bot.send_message(chat_id, 'Вы не играете')
                elif message.text in TicTakMarkup.sells and message.from_user.id != game.players[game.curent_players]:
                    bot.send_message(chat_id, 'Не ваш ход!')

            #TicTac



print('Bot start!')
bot.send_message(chat_id, 'Привет!\nНабери /help для вызова комманд.\nНабери /start для выбора игр.')
bot.infinity_polling()
bot.send_message(chat_id, 'Пока, я пошёл! Увидимся позже!')