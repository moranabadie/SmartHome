import time

from bs4 import BeautifulSoup
import requests

def read_anec(engine):
    try:
        r = requests.get("http://secouchermoinsbete.fr/random")
    except:
        
        return 1
    try:
        splitt = r.text.split('<div class="anecdote-content-wrapper">')
        splitt = splitt[1].split('<p class="summary">')
        splitt = splitt[1].split('>')
        splitt = splitt[1].split('<')
        text = splitt[0]    
        soup = BeautifulSoup(text, "html.parser")
        text= soup.get_text()
         
        engine.say("Je vais vous raconter une anecdote." )
        engine.runAndWait()
        time.sleep(0.4)
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.8)
    except:
        
        return 1