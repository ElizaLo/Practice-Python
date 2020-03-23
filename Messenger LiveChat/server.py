from flask import Flask
from datetime import datetime
from datetime import date
from datetime import time

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello everybody! " \
           "\n\n Welcome to LiveChat"

@app.route("/status")
def status():
    curr_date = date.today()
    curr_time = str(datetime.time(datetime.now()))

    return {
        'status': True,
        'name': 'LiveChat',
        'date': curr_date,
        'time': curr_time,
    }

app.run()
