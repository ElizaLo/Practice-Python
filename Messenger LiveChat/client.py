import requests

'''
responce = requests.get('http://127.0.0.1:5000/status')
print(responce.status_code)
print(responce.text)
print(responce.json())


message = { 'username': 'Ju', 'text': 'Hello'}
responce = requests.post('http://127.0.0.1:5000/send', json = message)
print(responce.status_code)
print(responce.text)
print(responce.json())
'''

def send_message(username, password, text):
    message = {'username': username, 'password': password, 'text': text}
    responce = requests.post('http://127.0.0.1:5000/send', json = message)
    return responce.status_code == 200


username = input('Enter your Name: ')
password = input('Enter password: ')

while True:
    text = input()
    result = send_message(username, password, text)
    if result is False:
        print('Error')
