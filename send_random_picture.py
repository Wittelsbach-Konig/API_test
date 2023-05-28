import requests

from kittybot import bot, chat_id

URL = 'https://api.thecatapi.com/v1/images/search'


if __name__ == '__main__':
    response = requests.get(URL).json()
    text = 'Вам телеграмма!'
    bot.send_message(chat_id, text)
    bot.send_photo(chat_id, response[0].get('url'))
