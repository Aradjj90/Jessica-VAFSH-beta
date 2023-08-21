import schedule
import Rooms
import serial
import threading
import General_command
import sys
import TTS
import Answer_Dictionary as say
import Dict_command
import Verification
import Sound_switching
import datetime

tts = TTS.TTS()


try:
    serial_com = serial.Serial('COM3', 115200)
except serial.serialutil.SerialException:  # Arduino is not connected
    Verification.bit_table['arduino']['ESP_connected'] = 1
    #tts.speak(say.get('arduino_Error'))
except NameError:  # another Arduino Error
    Verification.bit_table['arduino']['send_data'] = 1
    tts.speak(say.get('arduino_Error'))


# serialcom.timeout = 1

def onrRead():
    rx = serial_com.readline()
    comands = str(rx, 'utf-8').strip()
    data = comands.split(',')
    print(data)


def serialSend(data):
    txs = ""
    for val in data:
        txs += str(val)
        txs += ','
    txs = txs[:-1]
    txs += ';'
    print(txs)
    serial_com.write(txs.encode())


def start_greeting():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        tts.speak("Good Morning!")
    elif 12 <= hour < 18:
        tts.speak("Good Afternoon!")
    else:
        tts.speak("Good Evening!")
    tts.speak("I'm a voice assistant - Jessica! Please tell me what you wish")



if __name__ == "__main__":
    bedroomMam = Rooms.Room(index_of_input_device=1, anchor="bedroomMam")
    #bedroomMy = Rooms.Room(index_of_input_device=3, anchor="bedroomMy")
    threading.Thread(target=bedroomMam.vosk_voice_detector, daemon=True).start()
    #threading.Thread(target=bedroomMy.vosk_voice_detector, daemon=True).start()

    class_specimen = {'bedroomMam': bedroomMam,   # Розкоментувати коли добавить кімната
                      #'bedroomMy': bedroomMy
                      #'kitchen': kitchen,
                      #'hallway': hallway,
                      #'livingRoom': livingRoom,
                      }


    # start_greeting()
    while True:

        #print(str(bedroomMam.get_detection()))
        # print(object.get_respond())
        # print(Dict_command.get_dict_sys_answer(object.get_anchor()))
        # закрити програму
        #if General_command.return_Command_off():
            #Sound_switching.dic_foo['default']()
            #tts.speak(say.get('off'))
            #sys.exit()



        # Опрацювання загальної команди
        if General_command.var.get_flag():
            #Sound_switching.dic_foo[General_command.var.get_anchor()]()
            tts.speak(General_command.var.get_answer())
            General_command.var.set_end_flag_answer()
            if General_command.var.sysoff:
                sys.exit()

        for index in Dict_command.arduino_com.keys():
            if Dict_command.get_dict_sys_flag(index):
                if Rooms.MainRoom.write:
                    #Sound_switching.dic_foo[index]()  # switch audio device
                    class_specimen[index].set_skip(True)
                    tts.speak(say.get(Dict_command.get_dict_sys_answer(index)))  # say
                    class_specimen[index].set_skip(False)
                    Dict_command.set_dict_flag_done(index)  # change flag
                    # print('wright note')
                else:
                    #pass
                    #serialSend(Dict_command.get_dict_arduino_send(index))  # send to Grand ESP32 !!!!
                    #Sound_switching.dic_foo[index]()  # switch audio device
                    class_specimen[index].set_skip(True)
                    tts.speak(say.get(Dict_command.get_dict_sys_answer(index)))  # say
                    class_specimen[index].set_skip(False)
                    Dict_command.set_dict_flag_done(index)  # change flag

        #schedule.every().day.at('00:00').do(sleep_automode)  # вмконувати функцію в певний час
        #schedule.every().day.at('06:30').do(sleep_automode)  # вмконувати функцію в певний час

       


        # print(threading.active_count())
        # print(val == dic)
        # tts.speak(answer.get('off'))

