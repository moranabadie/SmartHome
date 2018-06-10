import datetime
import random
import time

import pyttsx3

from Threads.Anec.readDailyAnec import read_anec
from Threads.Anec.readDailyJoke import read_daily
from Threads.Weather.weather import weather


BJR = ["Bonjour", "Salut", "salam","hey", "yo", "Bonsoir, euh, non, bonjour"]
REVEIL = ["Il faut se lever ! ", \
          "Reveil !", "Debout les feignasse", \
          "On se reveil plus vite que ça.",\
           "Toi même tu sais il faut se lever.", "On se reveil", "Debout"]
def waik_up_speaker(now):
    ENGINE = pyttsx3.init()
    voices = ENGINE.getProperty('voices')
    for voice in voices:
        if "french" in str(voice):
            ENGINE.setProperty('voice', voice.id)
            print("to french")
            break
        
    
    print("La date est ok : str 0")
    ENGINE.say(BJR[random.randint(0,len(BJR)-1)] +" !")
    print("La date est ok : str 1")
    ENGINE.runAndWait()
    print("La date est ok : str 2")
    time.sleep(0.2)
    ENGINE.say(REVEIL[random.randint(0,len(REVEIL)-1)] +" !")
    ENGINE.runAndWait() 
    time.sleep(0.2)
    ENGINE.say("Il est "+ str(now.hour) + " heure et " + str(now.minute) + " minutes")
    ENGINE.runAndWait() 
    print("La date est ok : str 3")
    time.sleep(0.2)
    weather(ENGINE)
    print("La date est ok : str 4")
    time.sleep(0.2)
    ENGINE.runAndWait()
    print("La date est ok : str 5")
    read_anec(ENGINE)
    print("La date est ok : str 6")
    read_daily(ENGINE)
    print("La date est ok : str 7")

if __name__ == "__main__":
    now = datetime.datetime.now()
    waik_up_speaker(now)

