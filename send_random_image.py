# kittybot/send_random_image.py
import requests  # Импортируем библиотеку для работы с запросами.
from telebot import TeleBot


bot = TeleBot(token='5665092908:AAEFjVm-VAACr3MTE38ICrDUBXgY2QQXbX4')


chat_id = 920782568


URL = 'https://api.thecatapi.com/v1/images/search'

# Код запроса к thecatapi.com и обработку ответа обернём в функцию:
def get_new_image():
    response = requests.get(URL).json()
    random_cat = response[0].get('url')
    return random_cat


# Добавляем хендлер для команды /newcat:
@bot.message_handler(commands=['newcat'])
def new_cat(message):
    chat = message.chat
    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(commands=['start'])
def wake_up(message):
    chat = message.chat
    name = message.chat.first_name

    bot.send_message(
        chat_id=chat.id,
        text=f'Привет, {name}. Посмотри, какого котика я тебе нашёл',
    )

    bot.send_photo(chat.id, get_new_image())


@bot.message_handler(content_types=['text'])
def say_hi(message):
    chat = message.chat
    chat_id = chat.id
    bot.send_message(chat_id=chat_id, text='Привет, я KittyBot!')

bot.polling() 