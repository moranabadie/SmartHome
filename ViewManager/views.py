
from django.shortcuts import render

from ViewManager.models import Reveil


# Create your views here.
def home(request):
    t = Reveil.objects.all()
    
    return render(request, 'home.html',{"t" : t})