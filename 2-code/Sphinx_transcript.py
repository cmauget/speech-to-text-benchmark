import speech_recognition as sr # type: ignore

audio_file = "/home/cmauget/Bureau/Wikit/600898_short.wav"

class Sphinx_transcript:

    def __init__(self) -> None:
        self.r = sr.Recognizer()

    def transcript(self, audio_file):
        with sr.AudioFile(audio_file) as source:
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.record(source)  # read the entire audio file
        return self.r.recognize_sphinx(audio, language="fr-FR")

if __name__ == "__main__":
    test  = Sphinx_transcript()
    audio_file = "../1-input/600898_short.wav"
    print(test.transcript(audio_file))