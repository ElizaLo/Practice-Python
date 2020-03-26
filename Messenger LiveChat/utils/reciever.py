from datetime import datetime
import requests
import time

after = 0

def get_messages(after):
    responce = requests.get('http://127.0.0.1:5000/messages',
                            params={'after': after})
    data = responce.json()
    return data['messages']

def print_message(message):
    username = message['username']
    message_time = message['time']
    text = message['text']

    dt = datetime.fromtimestamp(message_time)
    dt_hms = dt.strftime('%H:%M:%S')

    print(dt_hms, username)
    print(text)
    print()


while True:
    messages = get_messages(after)

    if messages:
        after = messages[-1]['time']
        for message in messages:
            print_message(message)

    time.sleep(1)
