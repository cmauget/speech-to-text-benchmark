import speech_recognition as sr

audio_file = "/home/cmauget/Bureau/Wikit/600898_short.wav"

r = sr.Recognizer()
with sr.AudioFile(audio_file) as source:
    r.adjust_for_ambient_noise(source)
    audio = r.record(source)  # read the entire audio file

print(r.recognize_sphinx(audio, language="fr-FR"))