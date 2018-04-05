import speech_recognition as sr
from pprint import pprint
from os import path


def listen_user_says(my_key):
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
        print ('Done!')
    try:
        print("Microsoft Bing Voice Recognition thinks you said: ")
        # pprint(r.recognize_bing(audio, key=my_key, language="zh-CN", show_all=True))
        return r.recognize_bing(audio, key=my_key, language="zh-TW") 
    except sr.UnknownValueError:
        print("Microsoft Bing Voice Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))


