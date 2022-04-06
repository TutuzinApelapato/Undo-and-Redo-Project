from system import *
from visual import *


clearConsole = lambda: print('\n' * 150)


while True:
    try:
        option = menu(['ADD NEW TASK', 'LIST TASKS', 'UNDO TASK', 'REDO TASK', 'LEAVE FROM SYSTEM'])
        clearConsole()
        if option == 1:
            addTask()
        elif option == 2:
            listTasks()
        elif option == 3:
            undoTask()
        elif option == 4:
            redoTask()
        elif option == 5:
            leaveMessage()
            break
        else:
            formatText('ERROR! Try to enter a valid option.', 0, 1)
    except KeyboardInterrupt:
        clearConsole()
        formatText('ERROR! User preferred not to type anything.', 0, 1)
        break
    