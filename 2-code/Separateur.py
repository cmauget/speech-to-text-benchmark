import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
import torchaudio
import numpy as np
from speechbrain.pretrained import SepformerSeparation
from scipy.io.wavfile import write

class Separateur:
    def temps_en_m_s(self,time):
        minutes = time // 60000
        secondes = (time%60000)// 1000
        return minutes,secondes

    def split_silence(self,audio_file,nom_dossier):
        #Split un audio avec les silences
        
        sound_file = AudioSegment.from_wav(audio_file)
        audio_chunks = split_on_silence(sound_file, min_silence_len=500, silence_thresh=-33, keep_silence=5000 )
        dir_path = os.path.dirname(os.path.realpath(__file__))
        print(dir_path)
        time = 0

        for i, chunk in enumerate(audio_chunks):
            duration = int(len(chunk))
            time_m,time_s = self.temps_en_m_s(time)
            td_m,td_s = self.temps_en_m_s(time+duration)
            out_file = "{:02d}:{:02d}-{:02d}:{:02d}.wav".format(time_m,time_s,td_m,td_s)
            time = time +duration
            print("exporting", out_file)
            if not os.path.exists(nom_dossier):
                os.makedirs(nom_dossier)
            chunk.export(dir_path+"/"+nom_dossier+"/"+out_file, format="wav")


    def split_sb(self,audio_file):
        #Separe les audios des deux personnes renvoie un array d'audios (chaque i de l'array est une personne qui parle)
        print(audio_file)
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


    def export_np(self,audio_array , fs=8000):
        #Exporte les différentes personnes dans différents fichiers
        for i in range(np.shape(audio_array)[1]):
            scaled = np.int16(audio_array[:,i] / np.max(np.abs(audio_array[:,i])) * 32767)
            write('personne{0}.wav'.format(i), fs, scaled)
        return np.shape(audio_array)[1]



if __name__ == "__main__":
    file_path = "600898_short.wav"
    test = Separateur()
    audio=test.split_sb(file_path)
    test.export_np(audio)
    #test.split_silence("personne0.wav","p0")
    #test.split_silence("personne1.wav","p1")


#dir_path = os.path.dirname(os.path.realpath(__file__))
#audio_file = dir_path+"/600898_short.wav"
#audio_array=split_sb(audio_file)
#export_np(audio_array,2)