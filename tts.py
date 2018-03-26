# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:17:00 2018
Bing speech document: https://docs.microsoft.com/en-us/azure/cognitive-services/speech/api-reference-rest/bingvoiceoutput
@author: user
"""

import requests as req
import os
from xml.etree import ElementTree

# Access the token from api_key 
api_key = 'None'
headers = {'Ocp-Apim-Subscription-Key': api_key}
get_token = req.session()
access_token = get_token.post('https://api.cognitive.microsoft.com/sts/v1.0/issueToken', headers=headers).text

headers = {"Content-type": "application/ssml+xml",
           "X-Microsoft-OutputFormat": "riff-16khz-16bit-mono-pcm",
           "Authorization": "Bearer " + access_token}
# Changing voice output via SSML
body = ElementTree.Element('speak', version='1.0')
body.set('xml:lang', 'en-us')
voice = ElementTree.SubElement(body, 'voice')
voice.set('xml:lang', 'en-us')
voice.set('xml:gender', 'Female')
voice.set('name', 'Microsoft Server Speech Text to Speech Voice (zh-TW, Yating, Apollo)')
voice.text = "今天天氣很好，宗毅不開心，因為他在準備教案不能出去玩"
# 建立資料夾

get_record = req.session()

respond = get_record.post('https://speech.platform.bing.com/synthesize', data=ElementTree.tostring(body), headers=headers)

os.makedirs('./sounds', exist_ok=True)
with open('./sounds/' + 'test' + '.wav', 'wb') as f:
    f.write(respond.content)