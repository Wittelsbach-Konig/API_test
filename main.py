import os
from dotenv import load_dotenv
from pyrogram import Client


load_dotenv()


if __name__ == '__main__':
    api_id = os.getenv('api_id')
    api_hash = os.getenv('api_hash')
    app = Client('my_account', api_id, api_hash)
    app.start()
    app.send_message(637571435, 'Привет, это я, Тестовый бот!')
    app.stop()
