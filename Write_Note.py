import datetime
import Answer_Dictionary
import pickle
import random

d = {"reminder": ['to do somesing', 'go to cinema', ' buy medesin'],
     "program notebook": [],
     "general notebook": []
     }

'''
count = 1


inFile = open('note.txt', 'w')
inFile.close()
with open('note.txt', 'a') as inFile:
    while True:
        text = str(input())
        if 'stop' in text:
            count = 1
            break
        inFile.write(str(count) + " - " + text + "\n")
        count = count + 1

with open('note.txt') as inFile:
    print(inFile.read())

'''
# Запис/читання словника у текстовий файл.
# Словник містить об'єкти типу {int:str}


# 1. Задано словник - перелік днів тижня та їх номерів
D = {"reminder": [],
     "program notebook": ['1 - Перевести джеси на пайтон 3.8', '2 - Розібратися з написанням файлу'],
     "general notebook": ['1 - Має працювати']}

flags_dic = {'add': False, 'over write': False, 'deleted': False}

D2 = {}
D3 = ["Один","Два","Три"]
choice = ''

numerical_converter = {'one': 1,
                       'two': 2,
                       'three': 3,
                       'four': 4,
                       'five': 5,
                       'six': 6,
                       'seven': 7,
                       'eight': 8,
                       'nine': 9
                       }




def writefile():
    with open('note.txt', 'w') as f:
        # 2.2. Цикл запису елементів словника у файл
        for item in D:
            # 2.2.1. Сформувати рядок виду key:value
            s = str(item)  # взяти ключ як рядок
            s += ':'  # додати символ ':'
            arrey = D.get(item)
            for i in range(len(D.get(item))):
                s += str(i + 1) + ' - '
                s += arrey[i]
                if i < (len(D.get(item)) - 1):
                    s += ','
            s += '\n'  # додати символ нового рядка

            # 2.2.2. Записати рядок у файл
            f.write(s)


def riedfile():
    with open('note.txt', 'rt') as f:
        # 3.2. Створити пустий словник D2
        # 3.3. Читання даних з файлу та утворення нового словника
        for lines in f:  # Використати ітератор файлу
            # 3.3.1. Кожний підрядок lines - це елемент виду key:value
            # представлений у рядковому форматі.
            # Розбити lines на 2 підрядки
            strings = lines.split(':')

            # 3.3.2. Отримати ключ і значення
            key = str(strings[0])  # отримати ключ
            value = strings[1].rstrip()  # отримати значення без '\n'
            value = value.split(',')

            # 3.3.3. Додати пару key:value до словника D2
            D2[key] = value



def write_file_bin():
      file = open("notebook.bin", "wb")
      pickle.dump (d,file)
      file.close()


def ried_file_bin():
      file = open("notebook.bin", "rb")
      b = pickle.load(file)
      print(b)
      Answer_Dictionary.set_temp(b[choice])
      file.close()



def handler_mess(mess):
    global choice

    if 'reminder' in mess:
        choice = 'reminder'
        Answer_Dictionary.set_temp(
            f'You choice {choice}. What do you want to do? - add? - read? - deleted?')
        return 'temp'
    elif 'program notebook' in mess:
        choice = 'program notebook'
        Answer_Dictionary.set_temp(
            f'You choice {choice}. What do you want to do? - add? - read? - deleted?')
        return 'temp'
    elif 'general notebook' in mess:
        choice = 'general notebook'
        Answer_Dictionary.set_temp(
            f'You choice {choice}. What do you want to do? - add? - read? - deleted?')
        return 'temp'

    elif 'add' in mess:
        mess = mess.replace('add ', '')
        print(mess)
        try:
            d[choice].append(mess)
            flags_dic['add'] = True
            print(d[choice])
            Answer_Dictionary.set_temp(mess)
            return 'temp'
        except NameError:
            Answer_Dictionary.set_temp(
                'no category selected. choose a category: reminder, program notebook, general notebook')
            print('no category selected. ')
            return 'temp'

    elif 'yes' in mess and (flags_dic['add'] or flags_dic['deleted']):
        if flags_dic['add']:
            Answer_Dictionary.set_temp('ok') # перезаписати на 2 фрази
            return 'temp'
        if flags_dic['deleted']:
            d[choice].clear()
            Answer_Dictionary.set_temp(f'{choice} clean and now empty')

    elif 'no' in mess and (flags_dic['add'] or flags_dic['deleted']):
        if flags_dic['add']:
            try:
                d[choice].pope()
                print(d[choice])
                Answer_Dictionary.set_temp('scip. say what you want note')
                return 'temp'
            except NameError:
                Answer_Dictionary.set_temp(
                    'no category selected. choose a category: reminder, program notebook, general notebook')
                print('no category selected. ')
                return 'temp'
        if flags_dic['deleted']:
            Answer_Dictionary.set_temp('ok')  # перезаписати на 2 фрази
            return 'temp'

    elif 'read' in mess:
        if len(d[choice]) == 0:
            Answer_Dictionary.set_temp(f'dictionary{choice} is empty')
            return 'temp'
        ried_file_bin()
        return 'temp'

    elif 'over right' in mess:
        flags_dic['over write'] = True
        Answer_Dictionary.set_temp('say what you want')
        return 'temp'


def update_dict():
    pass


if __name__ == "__main__":
    print(len(d['reminder']))
    d['reminder'].clear()
    print(d['reminder'])

    #d['reminder'].append('python')
    #d['reminder'].append('Hello world!')
    #print(d['reminder'])

    #D2['reminder'] = D3
    #print(D2['reminder'])
