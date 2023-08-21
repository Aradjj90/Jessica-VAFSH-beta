import pyttsx3


class TTS:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialization TTS
        self.voices = self.engine.getProperty('voices')  # Collection of voices on the computer

    def speak(self, tts):
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 135)  # setting up new voice rate
        self.engine.say(tts)
        self.engine.runAndWait()

    def speak_UK(self, tts):
        self.engine.setProperty('voice', self.voices[2].id) # Natalia on 3, 2- Maruna
        self.engine.setProperty('rate', 160)  # setting up new voice rate
        self.engine.say(tts)
        self.engine.runAndWait()


if __name__ == "__main__":
    object = TTS()
    #object.speak_UK("команду прийнято і зроблено")
    object.speak("I can\'t understand what you mean")
