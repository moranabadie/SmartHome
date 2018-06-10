import datetime
import time

import requests

from SmartHome.settings import ID_USER_WEATHER


ID_city =  "6455259"
Id_user = ID_USER_WEATHER


def auxWeather(l):
    
    for i in l:
        if i == "Thunderstorm":
            return "Il y aura de l'orage"
    for i in l:
        if i == "Snow":
            return "Il y aura de la neige"       
    for i in l:
        if i == "Rain":
            return "Il y aura de la pluie"    
    for i in l:
        if i == "Drizzle":
            return "Il y aura de la brume"   
    
    for i in l:
        if i == "Clouds":
            return "Il y aura des nuages"   
    for i in l:
        if i == "Clear":
            return "Il fera beau"     
    return ""
    
def weather(mytext):
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast?id=" \
                 +ID_city + "&appid=" \
                 +Id_user)


    matin = []
    aprem = []
    soir = []
    matin_t = None
    aprem_t = None
    soir_t = None
    for l in r.json()["list"]:
        h = datetime.datetime.fromtimestamp(l["dt"]).hour
     
        if h > 6 and h <= 20:
            t =  l["main"]["temp"] - 273.15 
            
            
            
            main = l["weather"][0]["main"]
            
            if h < 12:
                if matin_t == None:
                    matin_t = int(t)
                matin.append(main)
            elif h < 18:
                if aprem_t == None:
                    aprem_t = int(t)
                aprem.append(main)
            else:
                if soir_t == None:
                    soir_t = int(t)
                soir.append(main)
        if h > 20:
            break
            
        
           
    matin = auxWeather(matin)
    if matin !="":
        mytext += matin +" ce matin"
    aprem = auxWeather(aprem)
    if aprem !="":
        mytext += aprem +" cette après-midi"
        
    soir = auxWeather(soir)
    if soir !="":
        mytext += soir +" ce soir"
       
    if matin_t != None:
        mytext += "Ce matin, il fera " + str(matin_t) + " degré" 
      
        
    if aprem_t != None:
        mytext += "Cet après-midi, il fera " + str(aprem_t) + " degré" 
      
    if soir_t != None:
        mytext += "Et ce soir, il fera " + str(soir_t) + " degré" 
    return mytext
        