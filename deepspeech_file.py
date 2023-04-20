# adapted from https://github.com/mozilla/DeepSpeech/blob/master/native_client/python/client.py
# which has a Mozzila Public License:
# https://github.com/mozilla/DeepSpeech/blob/master/LICENSE

from deepspeech import Model, version
import librosa as lr
import numpy as np
import os
 
# English model
scorer = "Models/deepspeech-0.9.3-models.scorer"
scorerES = "Models/kenlm_es.scorer"
# Spanish model
model = "Models/deepspeech-0.9.3-models.pbmm"
modelES = "Models/output_graph_es.pbmm"
# Italian model
modelIT = "Models/output_graph_it.pbmm"

# english Audio/////////////
audio_file = "Ex4_audio_files/EN/suitcase.wav"
# audio_file = "Ex4_audio_files/EN/sentence1.wav"
# audio_file = "Ex4_audio_files/EN/sentence2.wav"
# spanish audio
audio_fileES = "Ex4_audio_files/ES/suitcase_es.wav"
# Italian audio
audio_fileIT = "Ex4_audio_files/IT/where_it.wav"

assert os.path.exists(scorer), scorer + "not found. Perhaps you need to download a scroere  from the deepspeech release page: https://github.com/mozilla/DeepSpeech/releases"
assert os.path.exists(scorerES), scorerES + "not found. Perhaps you need to download a scroere  from the deepspeech release page: https://github.com/mozilla/DeepSpeech/releases"

assert os.path.exists(model), model + "not found. Perhaps you need to download a  model from the deepspeech release page: https://github.com/mozilla/DeepSpeech/releases"
assert os.path.exists(modelES), modelES + "not found. Perhaps you need to download a  model from the deepspeech release page: https://github.com/mozilla/DeepSpeech/releases"
assert os.path.exists(modelIT), modelIT + "not found. Perhaps you need to download a  model from the deepspeech release page: https://github.com/mozilla/DeepSpeech/releases"

assert os.path.exists(audio_file), audio_file + "does not exist"
assert os.path.exists(audio_fileES), audio_fileES + "does not exist"
assert os.path.exists(audio_fileIT), audio_fileIT + "does not exist"
# English
ds = Model(model)
ds.enableExternalScorer(scorer)
# Spanish
dsES = Model(modelES)
dsES.enableExternalScorer(scorerES)
# Italian
dsIT = Model(modelIT)

desired_sample_rate = ds.sampleRate()

desired_sample_rateES = dsES.sampleRate()

desired_sample_rateIT = dsIT.sampleRate()
# English
audio = lr.load(audio_file, sr=desired_sample_rate)[0]
audio = (audio * 32767).astype(np.int16) # scale from -1 to 1 to +/-32767
res = ds.stt(audio)
# Spanish
audioES = lr.load(audio_fileES, sr=desired_sample_rateES)[0]
audioES = (audioES * 32767).astype(np.int16) # scale from -1 to 1 to +/-32767
resES = dsES.stt(audioES)
# Italian
audioIT = lr.load(audio_fileIT, sr=desired_sample_rateIT)[0]
audioIT = (audioIT * 32767).astype(np.int16) # scale from -1 to 1 to +/-32767
resIT = dsIT.stt(audioIT)


# res = ds.sttWithMetadata(audio, 1).transcripts[0]
print(res)
print(resES)
print(resIT)




