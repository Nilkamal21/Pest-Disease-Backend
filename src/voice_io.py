import os
import queue
import json
import sounddevice as sd
import vosk
import pyttsx3

def init_tts(language_code='hi'):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    for voice in voices:
        if language_code in voice.id or language_code.encode() in voice.languages:
            engine.setProperty('voice', voice.id)
            break
    return engine

def speak(engine, text):
    engine.say(text)
    engine.runAndWait()

def recognize_speech(model_path, duration=5, samplerate=16000):
    q = queue.Queue()

    def callback(indata, frames, time, status):
        q.put(bytes(indata))

    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Vosk model not found at {model_path}")

    model = vosk.Model(model_path)
    rec = vosk.KaldiRecognizer(model, samplerate)

    with sd.RawInputStream(samplerate=samplerate, blocksize=8000, dtype='int16',
                           channels=1, callback=callback):
        print("Listening...")
        text = ""
        for _ in range(int(duration * samplerate / 8000)):
            data = q.get()
            if rec.AcceptWaveform(data):
                result = json.loads(rec.Result())
                text += " " + result.get("text", "")
        final_result = json.loads(rec.FinalResult())
        text += " " + final_result.get("text", "")
        print(f"Recognized: {text.strip()}")
        return text.strip()


if __name__ == "__main__":
    model_folder = 'models/vosk_hi'  # path to Hindi model
    tts_engine = init_tts('hi')

    speak(tts_engine, "कृपया अपनी फसल की समस्या बताएं")
    spoken_text = recognize_speech(model_folder, duration=7)
    speak(tts_engine, f"आपने कहा: {spoken_text if spoken_text else 'क्षमा करें, कुछ नहीं सुना'}")
