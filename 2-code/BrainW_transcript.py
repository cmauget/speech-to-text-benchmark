from speechbrain.pretrained import EncoderASR


class BrainW_transcript:

    def __init__(self):
        self.model = EncoderASR.from_hparams(source="speechbrain/asr-wav2vec2-commonvoice-fr", savedir="../models/speechbrain_models/asr-wav2vec2-commonvoice-fr")

    def transcript(self, audio_file):
        return self.model.transcribe_file(audio_file)



if __name__ == "__main__":
    test  = BrainW_transcript()
    audio_file = "../1-input/600898_short.wav"
    print(test.transcript(audio_file))

