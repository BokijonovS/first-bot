from telebot import TeleBot
from telebot.types import Message
bot = TeleBot('6996348885:AAHfwtQz0S2E9Hg9bzRZIe4NsQn5-Bus-7I')
@bot.message_handler(commands=['start'])
def start(message: Message):
    chat_id = message.chat.id
    full_name = message.from_user.full_name
    bot.send_message(chat_id, f'Assalomu alekum {full_name}')





bot.polling()

