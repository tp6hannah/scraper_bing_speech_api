# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:17:00 2018
Bing speech document: https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput
@author: user
"""

import requests as req
import os
from xml.etree import ElementTree
import pyaudio
import wave
import sys


def toSound(news_list,api_key):

    headers = {'Ocp-Apim-Subscription-Key': api_key}
    get_token = req.session()
    access_token = get_token.post('https://api.cognitive.microsoft.com/sts/v1.0/issueToken', headers=headers).text

    headers = {"Content-type": "application/ssml+xml",
            "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
            "Authorization": "Bearer " + access_token}

        # Changing voice output via SSML
    body = ElementTree.Element('speak', version='1.0')
    body.set('xml:lang', 'en-GB')
    voice = ElementTree.SubElement(body, 'voice')
    voice.set('xml:lang', 'en-GB')
    voice.set('xml:gender', 'Female')

    voice.set('name', 'Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)')

    # 建立資料夾
    get_record = req.session()
    os.makedirs('./output', exist_ok=True)
    

    i = 0
    for text in news_list:
        i+=1
        voice.text = text
        respond = get_record.post('https://speech.platform.bing.com/synthesize', data=ElementTree.tostring(body), headers=headers)
        
        audio_name = "news_"+ str(i)+ ".wav"
        with open('./output/' + audio_name, 'wb') as f:
            f.write(respond.content)

        # play the sound we just turn in

        CHUNK = 1024

        wf = wave.open("./output/"+audio_name, 'rb')

        p = pyaudio.PyAudio()

        stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

        data = wf.readframes(CHUNK)

        while len(data) > 0:
            stream.write(data)
            data = wf.readframes(CHUNK)

        stream.stop_stream()
        stream.close()

        p.terminate()

