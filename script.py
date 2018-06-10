import datetime
import random


from gtts.tts import gTTS

from Threads.Anec.readDailyAnec import read_anec
from Threads.Anec.readDailyJoke import read_daily
from Threads.Weather.weather import weather


BJR = ["Bonjour", "Salut", "salam","hey", "yo", "Bonsoir, euh, non, bonjour"]
REVEIL = ["Il faut se lever ! ", \
          "Reveil !", "Debout les feignasse", \
          "On se reveil plus vite que ça.",\
           "Toi même tu sais il faut se lever.", "On se reveil", "Debout"]
def waik_up_speaker(now):
    import os
 
    # The text that you want to convert to audio
     
    # Language in which you want to convert
    language = 'fr'
     
    # Passing the text and language to the engine, 
    # here we have marked slow=False. Which tells 
    # the module that the converted audio should 
    # have a high speed
    
     
    # Saving the converted audio in a mp3 file named
    # welcome 

    
    print("La date est ok : str 0")
    mytext = BJR[random.randint(0,len(BJR)-1)] +" !"
    mytext +=REVEIL[random.randint(0,len(REVEIL)-1)] +" !"
   
    mytext +="Il est "+ str(now.hour) + " heure et " + str(now.minute) + " minutes"
    
    mytext = weather(mytext)
   
    print("La date est ok : str 5")
    mytext = read_anec(mytext)
    print("La date est ok : str 6")
    mytext = read_daily(mytext)
    print("La date est ok : str 7")
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save("welcome.mp3")
     
    # Playing the converted file
    if os.name == 'nt':
        os.system("cmdmp3.exe welcome.mp3")
    else:
        os.system("amixer set PCM -- 93%")
        os.system("mpg123 welcome.mp3")
if __name__ == "__main__":
    now = datetime.datetime.now()
    waik_up_speaker(now)

