

import Dict_command
import Write_Note

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

    elif 'switcher off' in message or 'seizure off' in message or 'switching off' in message or 'swisher off' in message:
        print("automode off")
        Dict_command.arduino_com[anchor][2] = 0
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'night light' in message or 'night right' in message or 'nice light' in message or 'nice right' in message or 'night live' in message or 'night life' in message:
        print("nightlight on")
        if Dict_command.arduino_com[anchor][3] == 0:
            Dict_command.arduino_com[anchor][3] = 1
            Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com[anchor][3] = 0
            Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
            return True

    elif 'change' in message and ('light' in message or 'life' in message or 'right' in message):
        print("light mode change")
        if Dict_command.arduino_com[anchor][4] == 0:
            Dict_command.arduino_com[anchor][4] = 1
            Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com[anchor][4] = 0
            Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
            return True

    elif 'back light' in message or 'back right' in message or 'backlight' in message or 'bike light' in message:
        print("backlight on")
        if Dict_command.arduino_com[anchor][5] == 0:
            Dict_command.arduino_com[anchor][5] = 1
            Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com[anchor][5] = 0
            Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
            return True

    elif 'brightness plus' in message:
        print("brightness plus")
        Dict_command.arduino_com[anchor][6] = Dict_command.arduino_com[anchor][6] + 1
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'brightness minus' in message or 'brightness miles' in message or 'brightness minds' in message:
        print("brightness minus")
        Dict_command.arduino_com[anchor][7] = Dict_command.arduino_com[anchor][7] + 1
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif ('light' in message or 'right' in message or 'life' in message) and ('to' in message or 'too' in message) and 'hot' in message:
        print("light to hot")
        Dict_command.arduino_com[anchor][8] = Dict_command.arduino_com[anchor][8] + 1
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif ('light' in message or 'right' in message or 'life' in message) and ('to' in message or 'too' in message) and 'cold' in message:
        print("light to cold")
        Dict_command.arduino_com[anchor][9] = Dict_command.arduino_com[anchor][9] + 1
        Dict_command.set_dict_sys_on(anchor, 'turn', 'positive')
        return True

    elif 'right note' in message:
        Dict_command.set_dict_sys_on(anchor, 'wright note')
# _____________________________________________________________________________________________________________________

    elif 'tv on' in message:
        print("tv on")
        Dict_command.arduino_com['bedroomMy1'][1] = 1
        Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
        return True

    elif 'tv off' in message:
        print("tv off")
        Dict_command.arduino_com['bedroomMy1'][1] = 0
        Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
        return True

    elif 'source' in message:
        print("source")
        if Dict_command.arduino_com['bedroomMy1'][2] == 0:
            Dict_command.arduino_com['bedroomMy1'][2] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][2] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'menu up' in message or 'may you up' in message:
        print("menu up")
        if Dict_command.arduino_com['bedroomMy1'][3] == 0:
            Dict_command.arduino_com['bedroomMy1'][3] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][3] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'menu down' in message or 'may you down' in message:
        print("menu down")
        if Dict_command.arduino_com['bedroomMy1'][4] == 0:
            Dict_command.arduino_com['bedroomMy1'][4] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][4] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'menu ok' in message or 'may you okay' in message:
        print("menu ok")
        if Dict_command.arduino_com['bedroomMy1'][5] == 0:
            Dict_command.arduino_com['bedroomMy1'][5] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][5] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'five positions up' in message or 'five possession up' in message:
        print("five positions up")
        if Dict_command.arduino_com['bedroomMy1'][6] == 0:
            Dict_command.arduino_com['bedroomMy1'][6] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][6] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'five positions down' in message or 'five possession down' in message:
        print("five positions down")
        if Dict_command.arduino_com['bedroomMy1'][7] == 0:
            Dict_command.arduino_com['bedroomMy1'][7] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][7] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'two rolls down' in message or 'two girls down' in message or 'two blinds down' in message:
        print("two rolls down")
        if Dict_command.arduino_com['bedroomMy1'][8] == 0:
            Dict_command.arduino_com['bedroomMy1'][8] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][8] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'two rolls up' in message or 'two girls up' in message or 'two blinds up' in message:
        print("two rolls up")
        if Dict_command.arduino_com['bedroomMy1'][9] == 0:
            Dict_command.arduino_com['bedroomMy1'][9] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][9] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'right roll down' in message or 'right girl down' in message or 'right blinds down' in message or 'right lines down' in message:
        print("right rolls down")
        if Dict_command.arduino_com['bedroomMy1'][11] == 0:
            Dict_command.arduino_com['bedroomMy1'][11] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][11] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'right roll up' in message or 'right girl up' in message or 'right blinds up' in message or 'right lines up' in message:
        print("right rolls up")
        if Dict_command.arduino_com['bedroomMy1'][12] == 0:
            Dict_command.arduino_com['bedroomMy1'][12] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][12] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif (('left' in message or 'last' in message) and ('roll' in message or 'row' in message) and 'down' in message) or 'left blinds down' in message:
        print("left rolls down")
        if Dict_command.arduino_com['bedroomMy1'][13] == 0:
            Dict_command.arduino_com['bedroomMy1'][13] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][13] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif (('left' in message or 'last' in message) and ('roll' in message or 'row' in message) and 'up' in message) or 'left blinds up' in message:
        print("left rolls up")
        if Dict_command.arduino_com['bedroomMy1'][14] == 0:
            Dict_command.arduino_com['bedroomMy1'][14] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][14] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'table lamp' in message:
        print("table lamp")
        if Dict_command.arduino_com['bedroomMy1'][15] == 0:
            Dict_command.arduino_com['bedroomMy1'][15] = 1
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True
        else:
            Dict_command.arduino_com['bedroomMy1'][15] = 0
            Dict_command.set_dict_sys_on('bedroomMy1', 'turn', 'positive')
            return True

    elif 'first' in message:
        Dict_command.set_dict_sys_on(anchor, 'wright note')
        write_flag = True
        return True
