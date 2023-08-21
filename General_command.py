import time
import Dialogfow_bot
import datetime
import webbrowser
import Answer_Dictionary as say
import Write_Note


class variables():
    def __init__(self):
        self.flag_command = False
        self.info_say = ""
        self.timing = 0.0
        self.talk = False
        self.message = ""
        self.anchor = ""
        self.flag_note_write = False
        self.counter = 0
        self.counter = 0
        self.sysoff = False


    def get_flag(self):
        return self.flag_command

    def get_answer(self):
        return self.info_say

    def get_anchor(self):
        return self.anchor

    def get_talk(self):
        return self.talk

    def get_time(self):
        return self.timing

    def set_time(self, times):
        self.timing = times

    def set_talk(self, flag):
        self.talk = flag

    def set_answer(self, answer):
        self.info_say = answer

    def set_flag(self):
        self.flag_command = True

    def set_end_flag_answer(self):
        self.flag_command = False
        self.info_say = ""

    def set_flag_note_write(self):
        self.flag_note_write = True



var = variables()

def get_command(anchor, message):
    if 'jess off' in message or 'jessica off' in message or 'jesse off' in message or 'jess of' in message \
            or 'jesse of' in message or 'jesse of' in message:
        print("off")
        var.set_answer(say.get('off'))
        var.anchor = 'default'
        var.sysoff = True
        var.set_flag()
       # global sysoff
        #sysoff = True

    elif 'verification' in message:
        var.set_answer("catch")
    # ------------------------------------------------------------------------------------------------------------------

    if 'let\'s talk' in message:
        var.set_time(time.time())
        var.set_talk(True)
        print("Готова говорити")

    if var.get_talk():
        if len(message)>11:
            var.set_answer(Dialogfow_bot.chatbotmessage(message))
            var.set_flag()
            var.set_time(time.time())

    if time.time() - var.get_time() > 30.0 and var.get_talk():
        var.set_talk(False)
        print("time out")
    # ------------------------------------------------------------------------------------------------------------------

    if 'what time' in message or 'what time is it now' in message:
        now = datetime.datetime.now()
        var.set_answer("now is " + str(now.hour) + "..." + str(now.minute))
        var.anchor = anchor
        var.set_flag()

    elif ('open' in message) and ('hit a' in message or 'heat' in message or 'the' in message) and \
            ('fan' in message or 'fm' in message or 'radio' in message):
        webbrowser.open('http://online.hitfm.ua/HitFM_HD') # потрібно зайти в настройки бравзера і надати доступ щоб можна відтворювати звук
        var.set_answer(say.get('open', 'doing'))
        var.anchor = anchor
        var.set_flag()

'''
    elif 'right note' in message:
        var.set_answer('Write a note')
        var.set_flag()
        var.set_flag_note_write()

    if var.flag_note_write:
        Write_Note.handler_mess(message)


'''
