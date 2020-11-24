import telebot
from telebot import types

token = '1402248710:AAE_De0ZUFMLgWrQNprdq25KAlaPRtB5170'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.from_user.id, 'Киска здравствуй!')
    bot.send_message(message.from_user.id, 'Я разозлилась 😡')

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()