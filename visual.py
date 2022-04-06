from time import sleep

colors = ('\033[m',  # 0 = NO COLORS
    '\033[31m',  # 1 = RED
    '\033[32m',  # 2 = GREEN
    '\033[33m',  # 3 = YELLOW
    '\033[34m',  # 4 = BLUE
    '\033[35m',  # 5 = MAGENTA
    '\033[36m',  # 6 = CYAN
    '\033[37m',  # 7 = GREY
    '\033[97m'  # 8 = WHITE
    )


def formatText(phrase = 'TEXT', style=0, dye=0):
    lenght = len(phrase) + 4
    if style == 0:
        print(f'{colors[dye]}{phrase}{colors[0]}'.center(lenght))
    if style == 1:
        print(f'{colors[dye]}={colors[0]}' * lenght)
        print(f'{colors[dye]}{phrase}{colors[0]}'.center(lenght))
        print(f'{colors[dye]}={colors[0]}' * lenght)
    elif style == 2:
        print(f'{colors[dye]}~{colors[0]}' * lenght)
        print(f'{colors[dye]}{phrase}{colors[0]}'.center(lenght))
        print(f'{colors[dye]}~{colors[0]}' * lenght)
    if style == 3:
        print(f'{colors[dye]}-{colors[0]}' * lenght)
        print(f'{colors[dye]}{phrase}{colors[0]}'.center(lenght))
        print(f'{colors[dye]}-{colors[0]}' * lenght)
    if style == 4:
        print(f'{colors[dye]}{phrase}{colors[0]}'.center(lenght), end='')


def leaveMessage():
    sleep(1)
    formatText('LEAVING FROM SYSTEM.', 0, 6)
    sleep(1)
    formatText('LEAVING FROM SYSTEM..', 0, 6)
    sleep(1)
    formatText('LEAVING FROM SYSTEM...', 0, 6)
    sleep(1)
    