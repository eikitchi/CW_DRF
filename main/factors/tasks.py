import datetime
import os

import telebot
from celery import shared_task

from telegram import Bot

from config import settings
from main.factors.models import Factors


def get_common_chat_id(bot_token):
    """Функция получения chat_id по TELEGRAM_BOT_TOKEN"""
    bot = Bot(token=bot_token)
    updates = bot.getUpdates()

    if updates:
        chat_id = updates[-1].message.chat_id
        return chat_id

    return None


@shared_task
def send_reminders():
    # Получаем текущее время
    now = datetime.now()
    # Получаем список привычек, о которых нужно напомнить
    habits_to_remind = Factors.objects.filter(
        periodicity__gt=0,  # Выбираем привычки с положительной периодичностью
        time__hour=now.hour,  # Фильтруем привычки по текущему часу
        time__minute=now.minute,  # фильтруем привычки по текущей минуте
        of_publicity=True,  # Выбираем привычки с of_publicity=True
    )
    # Создаем экземпляр бота с использованием токена из настроек
    bot = telebot.TeleBot(os.getenv("TELEGRAM_BOT_TOKEN"), parse_mode=None)

    # Получаем chat_id с использованием токена бота

    telegram_chat_id = get_common_chat_id(settings.TELEGRAM_BOT_TOKEN)
    # Перебираем список привычек, которые нужно напомнить
    for habit in habits_to_remind:
        # Создаем текст сообщения с уведомлением о выполнении привычки
        message = f"Время выполнить привычку: {habit.activity}!"
        # Отправляем сообщение в общий чат в Telegram
        bot.send_message(chat_id=telegram_chat_id, text=message)