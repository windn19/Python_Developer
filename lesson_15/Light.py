# создать простейшего чат-бота в Telegram
# обработать ответы не менее, чем на 3 фразы и 3 команды.

import telebot

token = '...'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def welcam(message):
    bot.reply_to(message, 'Рад вас приветствовать!!!')


@bot.message_handler(commands=['admin'])
def admin_(message):
    if message.from_user.id == 911336813:
        bot.reply_to(message, 'Прювет, начальника')
    else:
        bot.reply_to(message, 'Чапай дальше, да побыстрее')


@bot.message_handler(commands=['gest'])
def know(message):
    bot.reply_to(message, 'Я тебе не служу, приятель')


@bot.message_handler(content_types=['text'])
def receive_from(message):
    text = message.text.lower()
    if 'месяц' in text:
        bot.reply_to(message, 'Месяц плюсом, месяц-минус - не беда')
    if 'год' in text:
        bot.reply_to(message, 'Год на год не приходится')
    if 'шаг' in text:
        bot.reply_to(message, 'Шаг за шагом, бог за богом')
    else:
        bot.reply_to(message, text.upper())


bot.polling()
