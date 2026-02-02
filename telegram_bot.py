import telebot
import requests

BOT_TOKEN = '8339258881:AAFHnSbxquQ82ndj37r_0P3uCvgUrbEL77Q'
API_URL = 'http://127.0.0.1:8000/api/register/'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(message):
    user_id = message.from_user.id
    username = message.from_user.username or f"user_{user_id}"

    try:
        response = requests.post(API_URL, json={
            'telegram_id': user_id,
            'username': username
        }, timeout=5)

        if response.status_code in (200, 201):
            bot.reply_to(message, "✅ Вы успешно зарегистрированы!")
        else:
            bot.reply_to(message, "❌ Ошибка регистрации.")
    except Exception:
        bot.reply_to(message, "❌ Не удалось подключиться к серверу.")

if __name__ == '__main__':
    bot.polling()