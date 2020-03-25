import time
from flask import Flask, request, abort
from datetime import datetime
# from datetime import date


app = Flask(__name__)


messages = [
    {'username': 'Li', 'text': 'Hello', 'time': 0.0}
]

users = {
    'Li': '123456'
}


@app.route("/") # decorator
def hello():
    return "Hello everybody! " \
           "\n\n Welcome to LiveChat"


@app.route("/status")
def status():
    #curr_date = date.today()
    datetime.now().strftime('%Y/%m/%d %H:%M:%S')

    return {
        'status': True,
        'name': 'LiveChat',
        #'date': curr_date,
        'time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
    }


@app.route("/send", methods = ['POST'])
def send():
    '''
    принимаем JSON
    {
        "username": str,
        "password": str,
        "text": str,
    }
    :return: JSON {"ok": true}
    '''
    username = request.json['username']
    password = request.json['password']

    if username in users: # зарегистрированный пользователь
        if password != users[username]: # авторизуем
            return abort(401)
    else: # новй пользователь
        users[username] = password # регистрируем

    text = request.json['text']
    current_time = time.time()
    message = {'username': username, 'text': text, 'time': current_time}
    messages.append(message)

    print(messages)

    return {"ok": True}


@app.route("/messages")
def messages_view():
    '''
    принимаем ?after=float
    :return: JSON   {
        "messages": [
            {"username": str, "text": str, "time": float},
            ...
        ]
    }
    '''
    after =  float(request.args.get('after'))

    # filtered_messages = []
    # for message in messages:
    #     if message['time'] > after:
    #         filtered_messages.append(message)

    # list comprehension
    filtered_messages = [message for message in messages if message['time'] > after]

    return {
        'messages': filtered_messages
    }




app.run()
