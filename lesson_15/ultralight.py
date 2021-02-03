# создать простейшего чат-бота в Telegram

import telebot

token = '1551764899:AAExHBckU96VmJHkZt9OTAo4Xb0UGKj6c58'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def wellcame(message):
    bot.reply_to(message, 'Рад вас приветствовать!!!')


bot.polling()
