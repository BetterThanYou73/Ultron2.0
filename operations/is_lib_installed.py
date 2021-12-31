import os

is_installed2 = ''

try:
    with open('operations/is_lib2_installed.txt','r') as file:
        is_installed2 = file.read()

except FileNotFoundError:
        with open('operations/is_lib2_installed.txt','w') as file:
            os.system('python -m pip install opencv-python')
            file.write('True')

if is_installed2 == 'False':
    with open('operations/is_lib2_installed.txt','w') as file:
        os.system('python -m pip install opencv-python')
        file.write('True')

is_installed = ''

try:
    with open('operations/is_lib_installed.txt','r') as file:
        is_installed = file.read()

except FileNotFoundError:
        with open('operations/is_lib_installed.txt','w') as file:
            os.system('python -m pip install pyautogui')
            file.write('True')

if is_installed == 'False':
    with open('operations/is_lib_installed.txt','w') as file:
        os.system('python -m pip install pyautogui')
        file.write('True')