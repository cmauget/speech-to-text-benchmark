from speechbrain.pretrained import EncoderDecoderASR


class Brain_transcript:

    def __init__(self):
        self.model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-commonvoice-fr", savedir="../models/speechbrain_models/asr-crdnn-commonvoice-fr")
        
    def transcript(self, audio_file):
        return self.model.transcribe_file(audio_file)



if __name__ == "__main__":
    test  = Brain_transcript()
    audio_file = "../1-input/600898_short.wav"
    print(test.transcript(audio_file))

