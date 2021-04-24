import pyautogui
import sys
import time
import string
import random
import datetime
from functions import *

path = os.path.abspath(os.getcwd())
filepath = (f'{path}\data\class.json')

#sys.path.append("C:/yourpath/AutomatedZoom")
screenWidth, screenHeight = pyautogui.size()

LoginScreen()
question = str(input("""      Başlatmak için başlat ya da 'b' yazınız       
Önerilen ayarları görmek için ayarlar veya 'a' yazınız\n
                    """))   # write 'b' or 'başlat', 'a' or 'ayarlar' to see recommended settings

if question.lower() == 'başlat' or question.lower() == 'b' and DoesZoomRunning() == True:
    print("""                ...BAŞLATILIYOR...               """)
    time.sleep(2)
    starting_time = input('███████ DERS BAŞLANGIC SAATİ: (XX:YY) ŞEKLİNDE ███████\n')     #meeting starting-time
    cL = int(input('███████ DERSLER KAÇ DAKİKA SÜRÜYOR: ███████\n'))                    #how does meeting last long, -minutes-  
    class_break = int(input('███████ TENEFÜS KAÇ DAKİKA: ███████\n'))                   #how does the break last long, -minutes-

    ImportToJson()        #get meeting information

    IDList = []
    PWDList = []
    NameList = []
    cM = cL * 60

    with open(filepath, "r") as json_dosya:
        veriler = json.load(json_dosya)
        for data in veriler['details']:
            IDList.append(data["ID"])
            PWDList.append(data["Password"])
            NameList.append(data["DERS"])

    a = True
    #b = True
    while a:
        try:
            if Time() == starting_time:     #if current time hits starting time, join meeting
                print('DERSE KATILIYOR')
                ExecuteZoom()
                time.sleep(6)
                JoinMeeting(
                    meeting_id=IDList[0],
                    meeting_password=PWDList[0],
                    meeting_name=NameList[0]
                )
                #join-meeting
                for j in range(0, cM):
                    time.sleep(1)

                    if j != 0:
                        print(
                            f"""\r<<< ŞUANKİ DERS: {NameList[0]} >>> █ <<< SAAT: {Time()} >>> █ <<< SONRAKİ DERS: {NameList[0]} >>> █ """,
                            end=""
                        )

                    elif j == cM - 1:
                        TerminateZoom()
                        pass

                a = False
            elif Time() != starting_time:
                time.sleep(1)
                print("""███ DERS İÇİN BEKLENİYOR ███""", end="")

        except:
            pass

    d = True
    cB = class_break * 60

    while d:
       for x in range(0, cB):
        time.sleep(1)

        if x != 0:
            time.sleep(1)
            print(f"""███ TENEFÜS ARASI ███""", end=" ")

        elif x == cB - 1:
            d = False

    e = True
    while e:
        try:
            if Time() == starting_time:
                print('DERSE KATILIYOR')
                ExecuteZoom()
                time.sleep(6)
                JoinMeeting(
                    meeting_id=IDList[0],
                    meeting_password=PWDList[0],
                    meeting_name=NameList[0]
                )
                # join-meeting
                for j in range(0, cM):
                    time.sleep(1)

                    if j != 0:
                        print(
                            f"""\r<<< ŞUANKİ DERS: {NameList[0]} >>> █ <<< SAAT: {Time()} >>> █ <<< SONRAKİ DERS: {NameList[0]} >>> █ """,
                            end=""
                        )

                    elif j == cM - 1:
                        TerminateZoom()
                        pass

                a = False
            elif Time() != starting_time:
                time.sleep(1)
                print("""███ DERS İÇİN BEKLENİYOR ███""", end="")
        except:
            pass

elif question.lower() == 'ayarlar' or question.lower() == 'a':
    print("""               ÖNERİLEN AYARLAR          
1) Zoom'a kullanıcı girişi yapılmalıdır
2) Zoom>Settings>Audio>Mute my mic... ve Zoom>Settings>Video>Turn off my video... işaretlerinin seçili olması                                                  
3) Ekranda zoom penceresinin sürekli açık, diğer pencerelerin üstünde ve pencere boyutunun en az ekranın 1/3ü kadar olması
4) Program tek çeşit dersten 2 ders saati olarak hazırlanmıştır
5) Bilgisayarda başka işlem yapılmaması tavsiye edilir
        """)

else:
    print("             Önce Zoom'u çalıştırın.         ")
