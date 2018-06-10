import random
import time
import requests

RANDOMPLUS = ["", "LOL", "MDR", "C'est très drôle non ?", "XPTDR"]
def read_daily(engine):
    try:
        r = requests.get("http://www.une-blague.com/la-blague-du-jour.html")
    except:
        return 1
    splitt = r.text.split('<h2 id="texte">')
    if len(splitt) > 1:
        croped = splitt[1]
        splitt = croped.split('</h2>')
        if len(splitt) > 0:
            croped = splitt[0].replace("<br>", "").replace("<br />", "").replace("<br >", "")
            croped = "Je vais vous raconter une blague que j'ai trouvé sur internet. " + croped
            
            time.sleep(0.8)
            engine.say(croped)
            engine.runAndWait()
            time.sleep(0.2)
            engine.say(RANDOMPLUS[random.randint(0,len(RANDOMPLUS)-1)] +".")
            engine.runAndWait()
            time.sleep(0.4)
            return 0
    return 1

