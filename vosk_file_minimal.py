
## ## https://github.com/alphacep/vosk-api/blob/master/python/example/test_microphone.py

#import argparse
import os
import queue
import vosk
import sys
import json
import wave 

#model_dir = "fr-40m"
model_dir = "en-us-40m"

if not os.path.exists(model_dir):
    print ("Please download a model for your language from https://alphacephei.com/vosk/models")
    print ("and unpack as "+model_dir+"' in the current folder.")
    sys.exit(0)

model = vosk.Model(model_dir) # load from a folder

with wave.open("commands.wav") as wf:
    assert wf.getnchannels() == 1, "must be a mono wav"
    assert wf.getsampwidth() == 2, "must be a 16bit wav"
    assert wf.getcomptype() == "NONE", "must be PCM data"
    
    rec = vosk.KaldiRecognizer(model, wf.getframerate())
    while True:
        data = wf.readframes(4000)
        if rec.AcceptWaveform(data):
            res = json.loads(rec.Result())
            print(res["text"])
            break


