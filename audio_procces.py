import speech_recognition as sr
import audio_input

def procces(filename):
    audio_input.input()
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data)
        return text
