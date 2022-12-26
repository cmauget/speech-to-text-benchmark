import sounddevice as sd

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
