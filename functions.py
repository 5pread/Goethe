import pyautogui
import time
import subprocess
import json
import os
import random

screenWidth, screenHeight = pyautogui.size()


def Time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    hour =(current_time[0]+ current_time[1])
    min = (current_time[3]+ current_time[4])
    return hour + ":" + min


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
        filepath = (f'{path}\icons')
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
                    𝒃𝒚 𝒍𝒖$𝒕                                 v1.0
                                                    """)


def ImportToJson():

    fs = input('███████ 1.DERS ADI: ███████\n ')
    fsID = input('███████ 1.DERS ID: ███████\n')
    fsPWD = input('███████ 1.DERS SIFRE: ███████\n')
    print('██████████████████████████████████████████')
    sc = input('███████ 2.DERS ADI: ███████\n ')
    scID = input('███████ 2.DERS ID: ███████\n')
    scPWD = input('███████ 2.DERS SIFRE: ███████\n')
    print('██████████████████████████████████████████')
    tc = input('███████ 3.DERS ADI: ███████\n ')
    tcID = input('███████ 3.DERS ID: ███████\n')
    tcPWD = input('███████ 3.DERS SIFRE: ███████\n')
    print('██████████████████████████████████████████')
    ft = input('███████ 4.DERS ADI: ███████\n ')
    ftID = input('███████ 4.DERS ID: ███████\n')
    ftPWD = input('███████ 4.DERS SIFRE: ███████\n')
    print('██████████████████████████████████████████')
    fifth = 'YOK'

    ders_dict = {
    "details" : [
        {
            "DERS": F"{fs}", "ID": F"{fsID}", "Password": F"{fsPWD}"
        },
        {
            "DERS": F"{sc}", "ID": F"{scID}", "Password": F"{scPWD}"
        },
        {
            "DERS": F"{tc}", "ID": F"{tcID}", "Password": F"{tcPWD}"
        },
        {
            "DERS": F"{ft}", "ID": F"{ftID}", "Password": F"{ftPWD}"
        },
        {
            "DERS": F"{fifth}", "ID": F"{fifth}", "Password": F"{fifth}"
        }
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


def RandomMessageOT():

    messages = [
        'hocam yoklama alırsanız ben buradayım ancak mikrofon açamıyorum',
        'hocam bağlantımda sıkıntı var sesim gelmeyebilir ben buradayım',
        'merhaba hocam ben yoklama alırsanız buradayım ancak mikrofonumu açamıyorum',
        'hocam merhaba ben buradayım müsait değilim mikrofon açamıyorum',
        'ben buradayım ancak mikrofon açamıyorum hocam eğer yoklama alırsanız',
        'mikrofonumda bir sıkıntı çıktı sesimi açamıyorum hocam eğer yoklama alırsanız buradayım',
        'müsait değilim mikrofon açamıyorum eğer yoklama alırsanız buradayım hocam'
    ]

    n = random.choice(messages)
    return n

