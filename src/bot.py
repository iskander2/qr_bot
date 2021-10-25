import os


import telebot
from flask import Flask, request

from config import TOKEN
from service import link_to_qr

server = Flask(__name__)
bot = telebot.TeleBot(TOKEN, parse_mode=None)


@server.route("/", methods=["POST"])
def receive_update():
    bot.process_new_updates(
        [telebot.types.Update.de_json(request.stream.read().decode("utf-8"))]
    )
    return {'ok': True}


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    path = link_to_qr(message.text)
    photo = open(path, 'rb')
    bot.send_photo(message.chat.id, photo)
    os.remove(path)


@server.route("/" + TOKEN, methods=["POST"])
def getMessage():
    bot.process_new_updates(
        [
            telebot.types.Update.de_json(
                request.stream.read().decode("utf-8")
            )
        ]
    )
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))