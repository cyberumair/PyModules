import platform
import pyautogui as gui
from main_msg import msg
from install_pkg import *

def get_input(purpose):
    supported_sys = ['Linux', 'Darwin', 'Windows']
    
    if platform.system() in supported_sys:
        install_pkg('pyautogui')
        output = gui.prompt(purpose)
        
    else:
        output = input(purpose)
        
    return output

if __name__ == '__main__':
    put = get_input('\nExample input: ')
    
    print(f'\nInput: {put}')
    print(f'\n{msg}\n')
