import datetime
import random
import time

from SmartHome.settings import ENGINE
from Threads.Anec.readDailyAnec import read_anec
from Threads.Anec.readDailyJoke import read_daily
from Threads.Weather.weather import weather
from ViewManager.models import Reveil


BJR = ["Bonjour", "Salut", "salam","hey", "yo", "Bonsoir, euh, non, bonjour"]
REVEIL = ["Il faut se lever ! ", \
          "Reveil !", "Debout les feignasse", \
          "On se reveil plus vite que ça.",\
           "Toi même tu sais il faut se lever.", "On se reveil", "Debout"]
class FakePointer():
    def __init__(self, v):
        self.v = v
        
def waik_up_process():
    
    
    
    t = Reveil.objects.all()
    for r in t:
    
        now = datetime.datetime.now()
        if r.date.hour == now.hour and r.date.minute == now.minute:
            print("La date est ok")
            waik_up_speaker(now)
            print("La date est ok : end")

def waik_up_speaker(now):
    ENGINE.say(BJR[random.randint(0,len(BJR)-1)] +" !")
    ENGINE.runAndWait()
    time.sleep(0.2)
    ENGINE.say(REVEIL[random.randint(0,len(REVEIL)-1)] +" !")
    ENGINE.runAndWait() 
    time.sleep(0.2)
    ENGINE.say("Il est "+ str(now.hour) + " heure et " + str(now.minute) + " minutes")
    ENGINE.runAndWait() 
    time.sleep(0.2)
    weather(ENGINE)
    time.sleep(0.2)
    ENGINE.runAndWait()
    read_anec(ENGINE)
    read_daily(ENGINE)
    