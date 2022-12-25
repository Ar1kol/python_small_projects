import os
import time
import requests
import schedule
from dotenv import load_dotenv

load_dotenv()
print(os.getenv("PHONE_NUMBER"),)

def send_message():
    resp = requests.post('https://textbelt.com/text', {
        'phone' : os.getenv("PHONE_NUMBER"),
        'message': 'Hey, Good morning',
        'key': 'textbelt'
    })
    print(resp.json())

# schedule.every().day.at('06:00').do(send_message)
schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)