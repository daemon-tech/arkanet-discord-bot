import os

def clear_():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')