from Room_Command import bedroomMam
from Room_Command import bedroomMy
from Room_Command import kitchen
from Room_Command import hallway
from Room_Command import livingRoom
import General_command


def processing(anchor, mess):
    if "bedroomMam" in anchor:
        answer = bedroomMam.get_command(anchor, mess)
        if answer is None:
            General_command.get_command(anchor, mess)
    elif "bedroomMy" in anchor:
        answer = bedroomMy.get_command(anchor, mess)
        if answer is None:
            General_command.get_command(anchor, mess)
    elif "kitchen" in anchor:
        answer = kitchen.get_command(anchor, mess)
        if answer is None:
            General_command.get_command(anchor, mess)
    elif "hallway" in anchor:
        answer = hallway.get_command(anchor, mess)
        if answer is None:
            General_command.get_command(anchor, mess)
    elif "livingRoom" in anchor:
        answer = livingRoom.get_command(anchor, mess)
        if answer is None:
            General_command.get_command(anchor, mess)


if __name__ == "__main__":
    # processing("bedroomMam", "")
    print(dict)
    processing("bedroomMam", "light on")
    # print(dic)
