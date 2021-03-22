import pyautogui
import sys
import time
import string
import random
from functions import *
import datetime

path = os.path.abspath(os.getcwd())
filepath = (f'{path}\data\class.json')

sys.path.append("C:/yourpath/AutomatedZoom")
screenWidth, screenHeight = pyautogui.size()

LoginScreen()
question = str(input("""      Başlatmak için başlat ya da 'b' yazınız       
Önerilen ayarları görmek için ayarlar veya 'a' yazınız\n
                    """))   # write 'b' or 'başlat', 'a' or 'ayarlar' to see recommended settings

if question.lower() == 'başlat' or question.lower() == 'b' and CheckZoomIsOpen() == True:     
    print("""                ...BAŞLATILIYOR...               """)
    time.sleep(2)
    starting_time = input('███████ DERS BAŞLANGIC SAATİ: (XX:YY) ŞEKLİNDE ███████\n')     #meeting starting-time
    cL = int(input('███████ DERSLER KAÇ DAKİKA SÜRÜYOR: ███████\n'))                    #how does meeting last long, -minutes-  
    class_break = int(input('███████ TENEFÜS KAÇ DAKİKA: ███████\n'))                   #how does the break last long -minutes-

    ImportToJson()        #get meeting information

    IDList = []
    PWDList = []
    NameList = []

    with open(filepath, "r") as json_dosya:
        veriler = json.load(json_dosya)
        for data in veriler['details']:
            IDList.append(data["ID"])
            PWDList.append(data["Password"])
            NameList.append(data["DERS"])

    t = datetime.datetime.now()
    current_time = str(t.hour) + ":" + str(t.minute)

    t2 = datetime.datetime.now() + datetime.timedelta(minutes=cL)
    end_time = str(t2.hour) + ":" + str(t2.minute)

    print(end_time)

    cM = cL * 60

    a = True
    b = True
    while a:
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
1) Zoom'a kayıt olup, kullanıcı girişinin yapılmış olması
2) Zoom ayarlarından meeting'e katıldığında otomatik olarak mikrofonun kapatılması ayarının yapılması                                                             
3) Ekranda zoom penceresinin sürekli açık, diğer pencerelerin üstünde ve pencere boyutunun en az ekranın 1/3ü kadar olması
4) Program 2 farklı ders üzerinden her ders 2 ders saati olmak üzere hazırlanmıştır, yani 4 ders saati vardır.
5) Bot çalışır iken bilgisayarda başka işlem yapılmaması tavsiye edilir. 
        """)

else:
    print("Önce Zoom'u çalıştırın.")
