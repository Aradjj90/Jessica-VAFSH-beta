import random

#import Dict_command

'''
Файл містить словник з різними відповідями на загальні теми
'''

dictionary = {'positive': ["Ok", "Ok, I do it", "As you wish", "command accepted and done"],
              'negative': ["I can\'t do that", "I\'m sorry but I won\'t do it", "Sorry, I can\'t"],
              'off': ["I am off, bye", "bye bye!", "Goodbye!", " See you soon!", "Great, I'm tired, bye",
                      "See you later"],
              'turn': ["Turn", "switched", "done"],
              'open': ["opened", "done"],
              'arduino_Error': ["ESP 32 si not connected", "I can\'t transfer data through the port",
                                "Check the ESP connection",
                                "Check if the ESP is connected to the correct USB port"],
              'dialogflow': ["I don\'t understand", "I can\'t understand what you mean",
                             "try to say it differently, I don\'t understand", "I don\'t know what to answer you",
                             "it is difficult for me to answer"],
              'doing': ["opening", "wait a second", "in processing", "i am doing"],
              'general': ["Wait a minute"],
              'wright note': ['preparation for recording. choose a category: reminder, program notebook, general notebook'],
              'temp': ['']
              }

def get(*key):
    print(key)
    cor = random.choice(key[0]) # із за того що параметр *key завертає параметри в кортеж( перед цим була ще 1 функція)
    try:
        answer = random.choice(dictionary.get(cor))
    except TypeError:
        cor = random.choice(key)
        answer = random.choice(dictionary.get(cor))
    return answer


def get1(*key):
    print(key)
    cor = random.choice(key)
    answer = random.choice(dictionary.get(cor))
    return answer


def get_specifically(index):
    return dictionary['general'][index]


def set_temp(mess):
    dictionary['temp'][0] = mess




if __name__ == "__main__":
    #print(dictionary['turn'][1])
    #print(get('mess'))
    set_temp('mess')
    print(get(''))
