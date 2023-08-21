# останні 2 індикси системні (передача флагу на відправку та текст озвучки)
# 10 індекс для переселання даних на інші плати
arduino_com = {'bedroomMam': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'bedroomMy': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'livingRoom': [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'hallway': [3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'kitchen': [4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'bathroom': [5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               'bedroomMy1': [6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
               }


def set_dict_sys_on(anchor, *answer):
    arduino_com[anchor][-1] = answer
    arduino_com[anchor][-2] = True


def set_dict_flag_done(anchor):
    arduino_com[anchor][-2] = False
    arduino_com[anchor][-1] = ""


def set_dict_answer(anchor, answer):
    arduino_com[anchor][-1] = answer


def get_dict_sys_answer(anchor):
    return arduino_com[anchor][-1]


def get_dict_sys_flag(anchor):
    return arduino_com[anchor][-2]


def get_dict_arduino_send(anchor):
    return arduino_com[anchor][:-2]


if __name__ == "__main__":
    # set_dict_sys_on('bedroomMam')
    arduino_com['bedroomMam'][0] = 'wright note'
