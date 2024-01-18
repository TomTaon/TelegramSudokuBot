import telebot
import sudoku
from config import TOKEN_KEY

TOKEN = TOKEN_KEY

bot = telebot.TeleBot(TOKEN)

games = {}


def client_status_check(id):
    if id in games:
        return True
    else:
        return False


@bot.message_handler(commands=['s', 'S'])
def send_response(message):
    global games

    if not client_status_check(message.chat.id):
        game_flag = False
    else:
        my_sudoku = games[message.chat.id]
        game_flag = my_sudoku.game_active

    if game_flag:
        bot.send_message(message.chat.id, "a game exists, to end it type /e")
    else:
        my_sudoku = sudoku.Board(message.chat.id, font_color="#0a7d5c")
        games[message.chat.id] = my_sudoku

        print(f"sender ID : {message.chat.id}")
        print("starting sudoku id", id(my_sudoku))

        file_name = my_sudoku.generate_starting_board_img()
        bot.send_photo(message.chat.id, photo=open(file_name, 'rb'))


@bot.message_handler(commands=['e', 'E'])
def send_response(message):
    global games

    print(f"sender ID : {message.chat.id}")

    if not client_status_check(message.chat.id):
        bot.send_message(message.chat.id, "there is no game to end \n create new game using /s")

    else:

        game_flag = games[message.chat.id].game_active

        if game_flag:
            print("closing sudoku id: ", id(games[message.chat.id]))

            games[message.chat.id].game_active = False

            bot.send_message(message.chat.id, "game ended\nto start a new game type /s")

        else:
            bot.send_message(message.chat.id, "there is no game to end \n create new game using /s")


@bot.message_handler(commands=['h', 'H'])
def send_response(message):
    print(f"sender ID : {message.chat.id}")
    bot.send_message(message.chat.id, "not made yet")


@bot.message_handler(func=lambda x: True)
def send_response(message):
    global games

    if not client_status_check(message.chat.id):
        bot.send_message(message.chat.id, r"to start sudoku game type /s")

    else:

        my_sudoku = games[message.chat.id]
        game_flag = my_sudoku.game_active

        if game_flag:

            msg_string = message.text
            works, response = my_sudoku.move(msg_string)
            if works:
                file_name = my_sudoku.generate_starting_board_img()
                bot.send_photo(message.chat.id, photo=open(file_name, 'rb'))

            else:
                bot.send_message(message.chat.id, response)

        else:
            bot.send_message(message.chat.id, r"to start sudoku game type /s")


# examples how to handle photo or document input
'''
@bot.message_handler(content_types=["photo"])
def send_response(message):
    print('message.photo = ', message.photo)

    file_id = message.photo[-1].file_id
    print('fileID = ', file_id)

    file_info = bot.get_file(file_id)
    print('file_info = ', file_info)

    file_path = file_info.file_path
    print('file.file_path = ', file_path)

    with open(file_id + ".jpg", 'wb') as file:
        file.write(bot.download_file(file_path))

    print("photo saved")
    bot.reply_to(message, f"photo saved to {os.getcwd()}")


@bot.message_handler(content_types=["document"])
def send_response(message):
    f_name = message.document.file_name
    print(f"file name: {f_name}")

    f_info = bot.get_file(message.document.file_id)
    print(f"file info: {f_info}")

    f_path = f_info.file_path
    print(f"file path: {f_path}")

    with open(f_name, 'wb') as file:
        file.write(bot.download_file(f_path))

    print("file saved")
    bot.reply_to(message, f"file saved to {os.getcwd()}")
'''

bot.polling()
