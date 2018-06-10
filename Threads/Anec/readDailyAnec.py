import time

from bs4 import BeautifulSoup
import requests

def read_anec(mytext):
    try:
        r = requests.get("http://secouchermoinsbete.fr/random")
    except:
        
        return mytext
    try:
        splitt = r.text.split('<div class="anecdote-content-wrapper">')
        splitt = splitt[1].split('<p class="summary">')
        splitt = splitt[1].split('>')
        splitt = splitt[1].split('<')
        text = splitt[0]    
        soup = BeautifulSoup(text, "html.parser")
        text= soup.get_text()
         
        mytext += "Je vais vous raconter une anecdote." 
        mytext += text
        return mytext
    except:
        
        return mytext