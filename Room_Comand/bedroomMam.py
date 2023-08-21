
import Dict_command
import Write_Note
from Open_weather import get_weather_now, call_forecast

write_flag = False


def get_command(anchor, message):
    global write_flag

    if write_flag:
        s = Write_Note.handler_mess(message)
        if s is not None:
            Dict_command.set_dict_sys_on(anchor, s)

    if 'light on' in message or 'right on' in message:
        print('light on')
        Dict_command.arduino_com[anchor][1] = 1
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'light off' in message or 'right off' in message or 'light of' in message or 'right of' in message:
        print('light off')
        Dict_command.arduino_com[anchor][1] = 0
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'switcher on' in message or 'seizure' in message:
        print("automode on")
        Dict_command.arduino_com[anchor][2] = 1
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'switcher off' in message or 'seizure off' in message or 'switching off' in message:
        print("automode off")
        Dict_command.arduino_com[anchor][2] = 0
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'first' in message:
        Dict_command.set_dict_sys_on(anchor, 'wright note')
        write_flag = True
        return True

    elif "what is the weather today" in message:
        Dict_command.set_dict_sys_on(anchor, call_forecast(0))

    elif "what is the weather now" in message or "what is the wiser now" in message:
        Dict_command.set_dict_sys_on(anchor, get_weather_now())

    elif "what is the weather tomorrow" in message:
        Dict_command.set_dict_sys_on(anchor, call_forecast(1))

    elif "what is the weather the day after tomorrow" in message:
        Dict_command.set_dict_sys_on(anchor, call_forecast(2))



