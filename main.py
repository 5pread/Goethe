import pyautogui
import sys
import time
import string
import random
from functions import *

path = os.path.abspath(os.getcwd())
filepath = (f'{path}\data\class.json')


def Time():
    time_ = time.localtime()
    current_time = time.strftime("%H:%M:%S", time_)
    hour = (current_time[0] + current_time[1])
    min = (current_time[3] + current_time[4])
    return hour + ":" + min


sys.path.append("C:/Users/sbsag/PycharmProjects/AutomatedZoom")
screenWidth, screenHeight = pyautogui.size()

LoginScreen()
question = str(input("""      Başlatmak için başlat ya da 'b' yazınız
Önerilen ayarları görmek için ayarlar veya 'a' yazınız\n
                    """))

if question.lower() == 'başlat' or question.lower() == 'b':
    print("""                ...BAŞLATILIYOR...               """)
    time.sleep(2)

    cS = input('███████ DERS BAŞLANGIC SAATİ: (XX:YY) ŞEKLİNDE ███████\n')
    cL = input('███████ DERSLER KAÇ DAKİKA SÜRÜYOR, TENEFÜS OLMADAN: ███████\n')
    cB = input('███████ TENEFÜS KAÇ DAKİKA: ███████\n')
    try:
        midbreak = input('███████ ÖĞLE TENEFÜSÜ VAR MI, EVET VEYA HAYIR: ███████\n')
        midbreakclass = int(input('███████ ÖĞLE TENEFÜSÜ KAÇINCI DERSTEN SONRA, TENEFÜS YOKSA BOŞ GEÇİN: ███████\n'))
        mbL = int(input('███████ ÖĞLE TENEFÜSÜ KAÇ DAKİKA SÜRÜYOR, TENEFÜS YOKSA BOŞ GEÇİN: ███████\n'))
        mbL = mbL * 60  # Transform middle-break minutes to seconds
    except ValueError or TypeError:
        pass

    cL = 60 * int(cL)  # Transform class minutes to seconds
    cB = 60 * int(cB)  # Transform class-break minutes to seconds

    ImportToJson()

    IDList = []
    PWDList = []
    NameList = []

    alphabet = []  # using alphabet for variables to use in loops
    string_alphabet = string.ascii_lowercase
    for i in string_alphabet:
        alphabet.append(i)
        break

    with open(filepath, "r") as json_dosya:
        veriler = json.load(json_dosya)
        for data in veriler['details']:
            IDList.append(data["ID"])
            PWDList.append(data["Password"])
            NameList.append(data["DERS"])


    def FirstClass(class_number, nextclass_number, starting_time):

        r = random.choice(alphabet)
        r = True

        class_number = int(class_number)
        nextclass_number = int(nextclass_number)

        while r:
            if starting_time == Time():
                ExecuteZoom()
                time.sleep(5)
                JoinMeeting(
                    meeting_id=IDList[class_number],
                    meeting_password=PWDList[class_number],
                    meeting_name=NameList[class_number]
                )

                for a in range(0, cL):
                    time.sleep(1)

                    if a != cL:

                        time.sleep(1)
                        print(
                            f"""\r<<< ŞUANKİ DERS: {class_number} >>> █ <<< SAAT: {Time()} >>> █ <<< SONRAKİ DERS: {nextclass_number} >>> █ """,
                            end=""
                        )

                        for her in range(0, 60):
                            time.sleep(1)
                            if her == 59:
                                OpenChat()
                                WriteChat(text=RandomMessageOT())
                                break
                            else:
                                print(f'time remaining for text >> {her}')


                    elif a == cL - 1:

                        time.sleep(1)
                        print(f'remaining time for class >>{a}')
                        TerminateZoom()
                        r = False
                        break

            elif cS != Time():
                time.sleep(10)
                print('Sonraki ders için bekleniyor...')


    def Class(class_numbernd, nextclass_numbernd):

        r = random.choice(alphabet)
        r = True

        class_numbernd = int(class_numbernd)
        nextclass_numbernd = int(nextclass_numbernd)

        while r:
            ExecuteZoom()
            time.sleep(5)
            JoinMeeting(
                meeting_id=IDList[class_numbernd],
                meeting_password=PWDList[class_numbernd],
                meeting_name=NameList[class_numbernd]
            )
            for b in range(0, cL):
                time.sleep(1)

                if b != cL:
                    time.sleep(1)
                    print(
                        f"""\r<<< ŞUANKİ DERS: {class_numbernd} >>> █ <<< SAAT: {Time()} >>> █ <<< SONRAKİ DERS: {nextclass_numbernd} >>> █ """,
                        end=""
                    )
                    for hre in range(0, 60):
                        time.sleep(1)
                        if hre == 59:
                            OpenChat()
                            WriteChat(text=RandomMessageOT())
                            break
                        else:
                            print(f'time remaining for text >> {hre}')
                    break

                if b == cL - 1:
                    time.sleep(1)
                    print(f'remaining time for class >>{b}')
                    TerminateZoom()
                    r = False
                    break


    if midbreak.lower() == 'evet':
        if midbreakclass == 3:
            FirstClass(0, 1, cS)
            Break(breaklong=cB)  # >>>> 1st class
            Class(0, 1)
            Break(breaklong=cB)
            Class(1, 2)
            MidBreak(midbreaklong=mbL)  # >>>> 2nd class
            Class(1, 2)
            Break(breaklong=cB)
            Class(2, 3)
            Break(breaklong=cB)  # >>>> 3nd class
            Class(2, 3)
            Break(breaklong=cB)
            Class(3, 4)
            Break(breaklong=cB)  # >>>> 4th class
            Class(3, 4)
        elif midbreakclass == 4:
            FirstClass(0, 1, cS)
            Break(breaklong=cB)  # >>>> 1st class
            Class(0, 1)
            Break(breaklong=cB)
            Class(1, 2)
            Break(breaklong=cB)  # >>>> 2nd class
            Class(1, 2)
            MidBreak(midbreaklong=mbL)
            Class(2, 3)
            Break(breaklong=cB)  # >>>> 3nd class
            Class(2, 3)
            Break(breaklong=cB)
            Class(3, 4)
            Break(breaklong=cB)  # >>>> 4th class
            Class(3, 4)
        elif midbreakclass == 5:
            FirstClass(0, 1, cS)
            Break(breaklong=cB)  # >>>> 1st class
            Class(0, 1)
            Break(breaklong=cB)
            Class(1, 2)
            Break(breaklong=cB)  # >>>> 2nd class
            Class(1, 2)
            Break(breaklong=cB)
            Class(2, 3)
            MidBreak(midbreaklong=mbL)  # >>>> 3nd class
            Class(2, 3)
            Break(breaklong=cB)
            Class(3, 4)
            Break(breaklong=cB)  # >>>> 4th class
            Class(3, 4)
        elif midbreakclass == 6:
            FirstClass(0, 1, cS)
            Break(breaklong=cB)  # >>>> 1st class
            Class(0, 1)
            Break(breaklong=cB)
            Class(1, 2)
            Break(breaklong=cB)  # >>>> 2nd class
            Class(1, 2)
            Break(breaklong=cB)
            Class(2, 3)
            Break(breaklong=cB)  # >>>> 3nd class
            Class(2, 3)
            MidBreak(midbreaklong=mbL)
            Class(3, 4)
            Break(breaklong=cB)  # >>>> 4th class
            Class(3, 4)
    elif midbreak.lower() == 'hayır':
        FirstClass(0, 1, cS)
        Break(breaklong=cB)  # >>>> 1st class
        Class(0, 1)
        Break(breaklong=cB)
        Class(1, 2)
        Break(breaklong=cB)  # >>>> 2nd class
        Class(1, 2)
        Break(breaklong=cB)
        Class(2, 3)
        Break(breaklong=cB)  # >>>> 3nd class
        Class(2, 3)
        Break(breaklong=cB)
        Class(3, 4)
        Break(breaklong=cB)  # >>>> 4th class
        Class(3, 4)



elif question.lower() == 'ayarlar' or question.lower() == 'a':
    print("""               ÖNERİLEN AYARLAR          
1) Zoom'a kayıt olup, kullanıcı girişinin yapılmış olması
2) Zoom ayarlarından meeting'e katıldığında otomatik olarak mikrofonun kapatılması' ayarının yapılması                                                             
3) Ekranda zoom penceresinin sürekli açık, diğer pencerelerin üstünde ve pencere boyutunun en az ekranın 1/3ü kadar olması
4) Program 4 farklı ders üzerinden her ders 2 ders saati olmak üzere hazırlanmıştır, yani 8 ders saati vardır.
5) Bot çalışır iken bilgisayarda başka işlem yapılmaması tavsiye edilir. 
        """)
