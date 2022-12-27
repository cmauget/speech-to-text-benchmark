import whisper # type: ignore

class Whisper_transcript:

    def __init__(self) -> None:
        self.model = whisper.load_model("base")

    def transcript(self, audio_file):
        result = self.model.transcribe(audio_file)
        return result["text"]

if __name__ == "__main__":
    test  = Whisper_transcript()
    audio_file = "../1-input/600898_short.wav"
    print(test.transcript(audio_file))