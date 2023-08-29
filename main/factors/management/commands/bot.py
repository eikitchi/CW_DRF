import os

import telebot

bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=None)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, я бот созданный для прививания привычек,выбери что ты хочешь ?\n"
                          "Напиши 'GO' для начала!")


@bot.message_handler(commands=['GO'])
def send_welcome(message):
    bot.reply_to(message, f"И так что я могу тебе предложить:\n"
                          f"1 - Создать привычку\n"
                          f"2 - Редактировать привычку\n"
                          f"3 - удалить привычку\n")


@bot.message_handler(commands=['stop'])
def send_welcome(message):
    bot.reply_to(message, "Понял,заканчиваем выработку привычек")


bot.infinity_polling()
