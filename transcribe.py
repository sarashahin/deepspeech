# ///////////////////////////////////////
# further Developments:
# //////////////////////////////////////
# //////////////////////////////////////

import speech_recognition as sr
from os import path
from pydub import AudioSegment


# transcribe audio file                                                         
audio_file = "Ex4_audio_files/EN/checkin.wav"
# audio_file = "Ex4_audio_files/EN/where.wav"

# use the audio file as the audio source                                        
recog = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
        audio = recog.record(source)  # read the entire audio file                  

        print("Transcription: " + recog.recognize_google(audio))