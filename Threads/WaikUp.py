import datetime
from subprocess import call

from ViewManager.models import Reveil
from SmartHome.settings import BASE_DIR



class FakePointer():
    def __init__(self, v):
        self.v = v
        
def waik_up_process():
    t = Reveil.objects.all()
    for r in t:
    
        now = datetime.datetime.now()
        if r.date.hour == now.hour and r.date.minute == now.minute:
            print("La date est ok")
            call(["python3", BASE_DIR + "/script.py"])
            print("La date est ok : end")


    