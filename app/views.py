from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topics(request):
    QST=Topic.objects.all()
    d={'topics':QST}
    return render(request,'display_topics.html',d)



def web(request):
    QSW=Webpage.objects.all()
    d={'webpage':QSW}
    return render(request,'web.html',d)

