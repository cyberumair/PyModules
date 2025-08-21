import importlib.util, os
from main_msg import msg

def check_install(pkg): # Check if a package is installed or not

    if importlib.util.find_spec(pkg) is None: # if pkg is not installed
        return True
        
    return False
        
def install(pkg):
    if check_install(pkg):     
        try:
            os.system(f'pip install {pkg}')

            if not(check_install(pkg)): # If package is installed correctly
                return pkg
                
            else: # If issues in installing the pkg
                return    
                
        except Exception as e: # If still there is something wrong
            print('\nSomething Went Wrong')
            print(f'\n{e}')
            exit() # Crash the program
            
    else: # If pkg is already installed
        return pkg
       
def install_pkgs(pkgs):
    pkg_installed = []
    redirect = '\n\t...\t...\t...'

    pkg_done = []
    
    for p in pkgs:
        if not(check_install(p)):
            pkg_done.append(1)

    if len(pkg_done) == len(pkgs):
        exit()

    else:
        print('\nInstalling the following Dependencies:')

        print('')
        for index, pkg in enumerate(pkgs): # Enumeration of list for index and value
            print(f'{index+1}.' , pkg)  
        print('')  

        for pkg in pkgs:
            result = install(pkg) # Stores pkg name

            if result: # If pkg name is something not None or Undefinded or False etc..
                pkg_installed.append(result)

        not_installed_pkgs = len(pkgs) - len(pkg_installed) # Number of Packages that are not installed

        if not_installed_pkgs == 0: # If all packages are installed
            print('✅ Done, All dependencies installed Successfully!')
            print(redirect)
        
        else: # if some packages not installed
            print(f'❗ Something Went Wrong, {not_installed_pkgs} dependencie(s) are (is) Not installed.')
            print('\tExiting, Try running the program again...\n')
            exit()

if __name__ == '__main__':
    install_pkgs(['colorama', 'pyautogui', 'pyjokes', 'qrcode']) # Example list
    print(f"\n{msg}\n") # Custom Msg
