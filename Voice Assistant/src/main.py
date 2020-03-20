import random
import playsound
from gtts import gTTS
import speech_recognition as sr


def listen():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Скажите команду:")
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        speech = r.recognize_google(audio, language="ru")
        print("Вы сказали: ", speech)
        return speech
    except sr.UnknownValueError:
        return 'Error'
    except sr.RequestError as e:
        return 'Error'



def say(text):
    voice = gTTS(text, lang = "ru")
    unique_filename = "audio_" + str(random.randint(0, 100000)) + ".mp3"
    voice.save(unique_filename)
    playsound.playsound(unique_filename)
    print("Assistant:", text)


def handle_message(message):
    message = message.lower()
    if "привет" in message:
        say("Привет-привет!")
    elif "прощай" in message:
        finish()
    else:
        say("Я такой команды не знаю")



def finish():
    print("Пока")
    exit()




if __name__ == '__main__':
    print('Test')


    while True:
        command = listen()
        handle_message(command)
