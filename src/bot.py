import telebot
from config import TOKEN
from service import link_to_qr
import os

bot = telebot.TeleBot(TOKEN,parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    path = link_to_qr(message.text)
    photo = open(path,'rb')
    print(path)
    bot.send_photo(message.chat.id,photo)
    os.remove(path)

bot.polling()