#!/usr/bin/env python3

import subprocess
import json

from vosk import Model, KaldiRecognizer, SetLogLevel


class Kaldi_transcript:

    def __init__(self):        
        self.SAMPLE_RATE = 16000
        SetLogLevel(0)
        self.model = Model("../models/vosk_model")
        self.rec = KaldiRecognizer(self.model, self.SAMPLE_RATE)


    def transcript(self,file_name):
        with subprocess.Popen(["ffmpeg", "-loglevel", "quiet", "-i",file_name,"-ar", str(self.SAMPLE_RATE) , "-ac", "1", "-f", "s16le", "-"],stdout=subprocess.PIPE) as process:
            final=""
            #print("new........................\n")
            while True:
                
                data = process.stdout.read(4000)
                if len(data) == 0:
                    break
                if self.rec.AcceptWaveform(data):                
                    inter =json.loads(self.rec.Result())['text']
                    final +=(" "+inter)
                    #print(inter)
                    
                else:
                    self.rec.PartialResult()
                    
            
            inter = json.loads(self.rec.FinalResult())['text']

            final +=(" "+inter)
            #print(inter)
            #print(self.rec.FinalResult())

            #print(final[14:len(final)-3])
            print(final)
            return final

if __name__ == "__main__":
    test = Kaldi_transcript()
    test.transcript("p1/00:00-00:03.wav")

