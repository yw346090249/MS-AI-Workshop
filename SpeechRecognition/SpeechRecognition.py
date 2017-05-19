#!/usr/bin/python
import speech_recognition as sr
import json
import os
from os import path

os.system("(arecord -f S16_LE -r 16000 try.wav&); sleep 3; kill -9 `pidof arecord`")
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "try.wav")

r = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source) 

BING_KEY = "BING SPEECH API SUBSCRIPTION KEY"  # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings

sentence =  r.recognize_bing(audio,key=BING_KEY)
print sentence.encode('utf-8')