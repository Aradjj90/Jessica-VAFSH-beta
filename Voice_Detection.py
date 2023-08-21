import speech_recognition as sr
import pyttsx3
import json
import os
import queue
import sounddevice as sd
import vosk
import sys


class VoiceFunction:
    def __init__(self, mode=False, audio_device=1, anchor="Спальня 1: "):
        self.r = sr.Recognizer()  # Initialization of Google voice recognition
        self.engine = pyttsx3.init()  # Initialization TTS
        self.voices = self.engine.getProperty('voices')  # Collection of voices on the computer
        self.q = queue.Queue()
        self.dump_fn = None
        self.flag_language = False
        self.mode = mode
        self.audio_device = audio_device
        self.model = vosk.Model("vosk-model-en-us-daanzu-20200905") # vosk-model-en-us-daanzu-20200905
        self.model_UK = vosk.Model("vosk-model-uk-v3") # vosk-model-uk-v3
        self.device_info = sd.query_devices(self.audio_device, 'input')
        self.samplerate = int(self.device_info['default_samplerate'])
        self.anchor = anchor
        self.respond = ""
        self.message = ""

    # Google TTS
    def google_voice_detector(self):
        with sr.Microphone(device_index=int(self.audio_device)) as source:
            print("Listning...")
            self.r.pause_threshold = 1
            self.r.adjust_for_ambient_noise(source)
            audio = self.r.listen(source)

        try:
            query = self.r.recognize_google(audio).lower()
            print(f"You said : {query}\n")
        except sr.UnknownValueError:
            print("sorry, i don't understand you")
            return 'None'
        except sr.RequestError:
            return 'None'
        return query

    def speak(self, tts):
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 135)  # setting up new voice rate
        self.engine.say(tts)
        self.engine.runAndWait()

    # Vosk TTS

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        self.q.put(bytes(indata))

    def getrespons(self):
        return self.respond

    def change_flag_language(self, flag):
        self.flag_language = flag

    def vosk_voice_detector(self):
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.audio_device, dtype='int16',
                               channels=1, callback=self.callback):

            print('#' * 80)

            rec = vosk.KaldiRecognizer(self.model, self.samplerate)
            rec_UK = vosk.KaldiRecognizer(self.model_UK, self.samplerate)

            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data) and self.flag_language == False:
                    y = (rec.Result())
                    texts = json.loads(y)
                    self.respond = (self.anchor + texts['text'])
                    print(self.getrespons())
                    if 'right note' in self.respond:
                        self.flag_language = True
                        print(self.flag_language)
                        print("Flag ON")
                if self.flag_language:
                    if rec_UK.AcceptWaveform(data):
                        y = (rec_UK.Result())
                        texts = json.loads(y)
                        self.respond = (self.anchor + texts['text'])
                        print(self.getrespons())
                    else:
                        x = (rec_UK.PartialResult())
                else:
                    x = (rec.PartialResult())

                if self.dump_fn is not None:
                    self.dump_fn.write(data)


if __name__ == "__main__":
    object = VoiceFunction()
    while True:
        object.vosk_voice_detector()
