import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import torchaudio
import numpy as np
from speechbrain.pretrained import SepformerSeparation
from scipy.io.wavfile import write

def split_silence(audio_file):
    sound_file = AudioSegment.from_wav(audio_file)
    audio_chunks = split_on_silence(sound_file, min_silence_len=500, silence_thresh=-33, keep_silence=5000 )
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for i, chunk in enumerate(audio_chunks):
        out_file = "chunk{0}.wav".format(i)
        print("exporting", out_file)
        chunk.export(dir_path+"/slice/"+out_file, format="wav")


def split_sb(audio_file):

    audio ,fs = torchaudio.load(audio_file)

    resampler = torchaudio.transforms.Resample(fs, 8000) 
    audio = resampler(audio)
    fs = 8000

    print("début séparation")
    separator = SepformerSeparation.from_hparams(source="speechbrain/sepformer-wsj02mix", savedir="./pretrained_sepformer")
    est_sources = separator.separate_batch(audio)
    print("Fin de séparation")

    audio_array = est_sources.numpy()[0] 
    
    return audio_array


def export_np(audio_array ,nb_pop ,fs=8000):

    for i in range(nb_pop):
        scaled = np.int16(audio_array[:,i] / np.max(np.abs(audio_array[:,i])) * 32767)
        write('personne{0}.wav'.format(i), fs, scaled)



dir_path = os.path.dirname(os.path.realpath(__file__))
audio_file = dir_path+"/600898_short.wav"
audio_array=split_sb(audio_file)
export_np(audio_array,2)



