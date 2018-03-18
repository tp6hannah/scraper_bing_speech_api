import speech_recognition as sr
from pprint import pprint
# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "audio.wav")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "french.aiff")
# AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "chinese.flac")

r = sr.Recognizer()

# use the audio file as the audio source
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file

with sr.Microphone() as source:
        print ('Say Something!')
        audio = r.listen(source)
        print ('Done!')
     
    
# recognize speech using Microsoft Bing Voice Recognition
BING_KEY = "your key"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
try:
    print("Microsoft Bing Voice Recognition thinks you said: ")
    pprint(r.recognize_bing(audio, key=BING_KEY, language="zh-CN", show_all=True))
except sr.UnknownValueError:
    print("Microsoft Bing Voice Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Microsoft Bing Voice Recognition service; {0}".format(e))


