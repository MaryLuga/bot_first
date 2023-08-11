import telebot
bot = telebot.TeleBot("6080573579:AAFQToJ_NQNHhHAQ24vJD85FZbSkFZPxzC8")
token = "6080573579:AAFQToJ_NQNHhHAQ24vJD85FZbSkFZPxzC8"
id = "1657110493"
import requests
import json
from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import MessageHandler
#from telegram.ext import Filters

def send(text):
    url = "https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+id+'&text='+text+'"
    resp = requests.get(url)
    r = resp.json()
    return

send("bitcoin")

print("hi")
#from aiogram import executor
#from app import telebot
#executor.start_polling(bot.dp,
#                       skip_updates=True,
#                       on_shutdown=telebot.on_shutdown)

#token = "6080573579:AAFQToJ_NQNHhHAQ24vJD85FZbSkFZPxzC8"

