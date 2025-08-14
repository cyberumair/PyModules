import pkgutil
import os
from main_msg import msg

def install_pkg(pkg):
    installed = pkgutil.find_loader(pkg) is not(None)
    default_msg = '\nNow, running the actual program...'

    if not(installed):
        print(f'\nInstalling {pkg}...')
        
        try:
            os.system(f'pip install {pkg}')
            print(f"\n'{pkg}' installed successfully!")
            print(default_msg)
        
        except Exception as e:
            print('\nSomething Went Wrong')
            print(f'\n{e}')
            exit() # Crash the program
    else:
        print(f"\n'{pkg}' is already Installed.")
        print(default_msg)
        
if __name__ == '__main__':
    install_pkg('pyjokes')
    print(f"\n{msg}\n")
