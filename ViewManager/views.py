
from django.shortcuts import render

from SmartHome.settings import ENGINE
from ViewManager.models import Reveil, Last


# Create your views here.
def home(request):
    t = Reveil.objects.all()
    n = Last.objects.first()
    if n == None:
        n = "Never"
    else:
        n = str(n.date)
    ENGINE.say('test')
    ENGINE.runAndWait()
    return render(request, 'home.html',{"t" : t, "n" : n})