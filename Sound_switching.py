import pyautogui


# alt + m - bedroomMam
# alt + y - bedroomMy
# alt + k - kitchen
# alt + h - hallway
# alt + l - livingRoom
# alt + d - default


def swich_bedroomMam_speeck():
    pyautogui.hotkey('alt', 'm')
    print("Сканало")


def swich_bedroomMy_speeck():
    pyautogui.hotkey('alt', 'y')
    print("Second output")


def swich_kitchen_speeck():
    pyautogui.hotkey('alt', 'k')


def swich_hallway_speeck():
    pyautogui.hotkey('alt', 'h')


def swich_livingRoom_speeck():
    pyautogui.hotkey('alt', 'l')


def swich_def_speeck():
    pyautogui.hotkey('alt', 'd')


dic_foo = {'bedroomMam': swich_bedroomMam_speeck,
           'bedroomMy': swich_bedroomMy_speeck,
           'kitchen': swich_kitchen_speeck,
           'hallway': swich_hallway_speeck,
           'livingRoom': swich_livingRoom_speeck,
           'default': swich_def_speeck,
           'bedroomMy1': swich_bedroomMy_speeck
           }

if __name__ == "__main__":
    dic_foo['bedroomMam']()
    dic_foo['bedroomMy']()

    '''
    val = int(input())
    print(val)
    if val == 1:
        swich_bedroomMam_speeck()
        print("нажав")
    if val == 2:
        swich_bedroomMy_speeck()
    if val == 3:
        swich_kitchen_speeck()
    if val == 0:
        swich_def_speeck()
    
    '''
