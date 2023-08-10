import requests
import json

token = "6080573579:AAFQToJ_NQNHhHAQ24vJD85FZbSkFZPxzC8"
id = "1657110493"

def send(text):
    url = "https://api.telegram.org/bot'+token+'/sendMessage?chat_id='+id+'&text='+text+'"
    resp = requests.get(url)
    r= resp.json()

send("bitcoin")
