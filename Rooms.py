import json
import os
import queue
import sounddevice as sd
import vosk
import sys
import Command_distributor
#import Mediapipe_face_detec
import threading
import Write_Note


class MainRoom:
    write = False


class Room(MainRoom):
    def __init__(self, index_of_input_device=0, anchor="", videoCapture=0):  # anchor - вказується назва кімнати
        self.index_of_input_device = index_of_input_device
        #self.face_detection = Mediapipe_face_detec.Mediapipe_face_detec(videoCapture)
        self.q = queue.Queue()
        self.dump_fn = None
        self.model_UK = "vosk-model-uk-v3"
        self.model = vosk.Model("vosk-model-en-us-daanzu-20200905")
        self.device_info = sd.query_devices(self.index_of_input_device, 'input')
        self.samplerate = int(self.device_info['default_samplerate'])
        self.anchor = anchor
        self.respond = ""
        self.list =[]
        self.skip = False

    def callback(self, indata, frames, time, status):
        """This is called (from a separate thread) for each audio block."""
        if status:
            print(status, file=sys.stderr)
        if not self.skip: # does not listen when talking
            self.q.put(bytes(indata))

    def get_respond(self):
        return self.respond

    def get_anchor(self):
        return self.anchor

    def set_skip(self, flag):
        self.skip = flag

    #def get_detection(self):
        #return self.face_detection.detection()


    def vosk_voice_detector(self):
        # запуск потоку з відео
        #threading.Thread(target=self.face_detection.face_detec, daemon=True).start()
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.index_of_input_device,
                               dtype='int16',
                               channels=1, callback=self.callback):

            print('#' * 80)

            rec = vosk.KaldiRecognizer(self.model, self.samplerate)
            while True:
                data = self.q.get()
                if rec.AcceptWaveform(data):
                    y = (rec.Result())
                    texts = json.loads(y)
                    self.respond = (texts['text'])
                    if 'first' in self.respond:
                        MainRoom.write = True
                    print(self.anchor + ": " + self.respond)
                    Command_distributor.processing(self.anchor, self.respond)
                else:
                    x = (rec.PartialResult())
                if self.dump_fn is not None:
                    self.dump_fn.write(data)

    def vosk_UA_voice_detector(self):
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, device=self.index_of_input_device,
                               dtype='int16',
                               channels=1, callback=self.callback):

            print('UA voice detection')

            model_UK = vosk.Model(self.model_UK)
            rec_UK = vosk.KaldiRecognizer(model_UK, self.samplerate)
            self.write = True
            while True:
                data = self.q.get()
                if rec_UK.AcceptWaveform(data):
                    y = (rec_UK.Result())
                    texts = json.loads(y)
                    self.respond = (texts['text'])
                    print(self.get_respond())
                    if len(self.respond) > 1:
                        self.list.append(self.respond)
                        print(self.list)
                else:
                    x = (rec_UK.PartialResult())
                if self.dump_fn is not None:
                    self.dump_fn.write(data)


if __name__ == "__main__":
    object = Room(index_of_input_device=0, anchor="bedroomMam")
    object.vosk_UA_voice_detector()

    while True:
        pass
