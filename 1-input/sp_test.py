from speechbrain.pretrained import EncoderDecoderASR
import speechbrain as sb
import audiofile as af
import sounddevice as sd
import matplotlib as plt
from pydub import AudioSegment
from pydub.silence import split_on_silence


audio_file = "/home/cmauget/Bureau/Wikit/600898.wav"
asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr", savedir="pretrained_models/asr-crdnn-commonvoice-fr")

def record_audio(filename, seconds):
    fs=16000
    print("recording in progress...")
    y = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()
    y=y.T
    af.write(filename, y, fs)
    print("saved")

def record(seconds):
    record_audio("temp.flac", seconds)
    audio_file = "temp.flac"
    return audio_file


for i in range(54):
    audio_file = "/home/cmauget/Bureau/Wikit//slice/chunk{0}.wav".format(i)
    out = asr_model.transcribe_file(audio_file)
    print(out)


