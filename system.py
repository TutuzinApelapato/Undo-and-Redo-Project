from visual import *
from time import sleep


total_list = []
temp_list = []


def menu(list):
    formatText('MAIN MENU', 1, 6)
    c = 1
    for item in list:
        sleep(0.5)
        formatText(f'{c} - {item}', 0, 3)
        c += 1
    print('\033[36m=\033[m' * 50)
    option = readInt('\033[36mYOUR OPTION > \033[m')
    return option


def readInt(txt):
    while True:
        num = input(txt)
        if num.isnumeric():
            num = int(num)
            return num
        else:
            formatText('ERROR! Try to enter a valid integer!', 0, 1)


def addTask():
    c = len(temp_list) + 1
    try:
        temp_list.append(f'Task {c}')
        total_list.append(f'Task {c}')
        formatText(f'Task {c} successfully added to list.', 0, 2)
    except:
        formatText('ERROR! While adding new task.', 0, 1)
    

def listTasks():
    for i in temp_list:
        formatText(i, 0, 4)


def undoTask():
    try:
        formatText(f'{temp_list[-1]} successfully undone.', 0, 2)
        temp_list.pop()
    except:
        formatText("There\'s no way to undo something that hasn\'t been done.", 0, 1)


def redoTask():
    if len(temp_list) < len(total_list):
        c = len(temp_list) + 1
        temp_list.append(f'Task {c}')
        formatText(f'Task {c} successfully redone.', 0, 2)
    else:
        formatText("There\'s no way to remake something that hasn\'t been done.", 0, 1)
        