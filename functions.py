import pyautogui
import time, datetime
import subprocess
import json
import os
import random

screenWidth, screenHeight = pyautogui.size()


def Time():
    current_time = datetime.datetime.now()
    now = current_time.strftime("%H:%M")
    return now

def LocateCursorPosition():
    print('Locating cursor in...')
    i = 4
    while True:
        time.sleep(1)
        i = i - 1
        print(i)
        if i == 0:
            break
        else:
            pass
    currentMouseX, currentMouseY = pyautogui.position()

    print(F'Location point: {currentMouseX}, {currentMouseY}')


def ClickLocation(x, y):
    time.sleep(3)
    pyautogui.click(x,y)
    print(f'Clicked on {x}, {y}')


def ExecuteZoom():
    time.sleep(2)
    try:
        env = os.getenv('APPDATA')
        subprocess.call([f'{env}/Zoom/bin/Zoom.exe'])
    except FileNotFoundError:
        print('Lütfen önce zoom kurun.')

def OpenChat():
    pyautogui.hotkey('alt', 'h')


def WriteChat(text):
    time.sleep(1)
    pyautogui.write(f'{text}', interval=0.10)
    time.sleep(10)
    pyautogui.hotkey('Enter')


def JoinMeeting(meeting_id, meeting_password, meeting_name):
    time.sleep(6)
    try:
        path = os.path.abspath(os.getcwd())
        filepath = f'{path}\icons'
        pyautogui.click(f'{filepath}/joinbutton.png')
        time.sleep(3)
        pyautogui.write(f'{meeting_id}', interval=0.25)
        pyautogui.click(f'{filepath}/joinbutton2.png')
        time.sleep(3)
        pyautogui.write(f'{meeting_password}', interval=0.25)
        time.sleep(3)
        pyautogui.click(f'{filepath}/joinmeeting.png')
        print(f"""████████████████ DERSE BAŞARIYLA KATILDI ████████████████
████████████████    ID: {meeting_id} NAME: {meeting_name}   ████████████████""")
    except:
        print('Bir şeyler ters gitti.')


def MuteUnmuteMyself():
    time.sleep(1)
    try:
        pyautogui.hotkey('alt', 'a')
    except:
        print('Şuan sustur/susturma yapamıyorum.')

def TerminateZoom():
    time.sleep(1)
    try:
        subprocess.call(["taskkill","/F","/IM","Zoom.exe"], stdout=subprocess.DEVNULL)
    except:
        print('Bir şeyler ters gitti')


def MoveCursor():
    while True:
        time.sleep(2)
        pyautogui.move(0, 5)
        time.sleep(2)
        pyautogui.move(0, -5)



def LoginScreen():
    print("""
 ██████╗  ██████╗ ███████╗████████╗██╗  ██╗███████╗
██╔════╝ ██╔═══██╗██╔════╝╚══██╔══╝██║  ██║██╔════╝
██║  ███╗██║   ██║█████╗     ██║   ███████║█████╗  
██║   ██║██║   ██║██╔══╝     ██║   ██╔══██║██╔══╝  
╚██████╔╝╚██████╔╝███████╗   ██║   ██║  ██║███████╗
 ╚═════╝  ╚═════╝ ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
                  𝒃𝒚 spread                                 v1.1.0
                                                    """)


def ImportToJson():

    fs = input('███████ DERS ADI: ███████\n ')
    fsID = input('███████ DERS ID: ███████\n')
    fsPWD = input('███████ DERS SIFRE: ███████\n')

    ders_dict = {
    "details" : [
        {
            "DERS": F"{fs}", "ID": F"{fsID}", "Password": F"{fsPWD}"
        },
    ]
    }

    p = os.path.abspath(os.getcwd())
    filepath = (f'{p}\data\class.json')

    with open(filepath, "w") as json_dosya:
        json.dump(ders_dict, json_dosya, indent=4)

    #with open(filepath, "r") as json_dosya:    #read data
        #veriler = json.load(json_dosya)
        #for ders in veriler:
            #print(ders)

def Break(breaklong):
    for x in range(0, breaklong):
        time.sleep(1)
        print(f"""\r█ <<< TENEFÜS / SAAT: {Time()} >>> █  """, end="")

def MidBreak(midbreaklong):
    for k in range(0, midbreaklong):
        time.sleep(1)
        print(f"""\r█ <<< ÖĞLE TENEFÜS / SAAT: {Time()} >>> █  """, end="")

def DoesZoomRunning():
    output = os.popen('wmic process get description, processid').read()
    #print(output)
    if 'Zoom.exe' in output:
        return True
    elif 'Zoom.exe' not in output:
        return False



