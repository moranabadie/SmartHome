
from django.shortcuts import render

from ViewManager.models import Reveil, Last


# Create your views here.
def home(request):
    t = Reveil.objects.all()
    n = Last.objects.first()
    if n == None:
        n = "Never"
    else:
        str(n.date)
    n = "tests"
    return render(request, 'home.html',{"t" : t, "n" : n})