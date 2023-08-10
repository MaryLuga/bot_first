import telebot
bot = telebot.TeleBot("6080573579:AAFQToJ_NQNHhHAQ24vJD85FZbSkFZPxzC8")
import requests
import json

#token = "6080573579:AAFQToJ_NQNHhHAQ24vJD85FZbSkFZPxzC8"
id = "1657110493"

def send(text):
    url = "https://api.telegram.org/bot'+bot+'/sendMessage?chat_id='+id+'&text='+text+'"
    resp = requests.get(url)
    r = resp.json()

send("bitcoin")
print("hi")