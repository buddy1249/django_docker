from django.shortcuts import render
from .models import Agnks

# Create your views here.

def index(request):

    w = Agnks.objects.all()  
    
    data = {       
        'w': w,       
        }
    return render(request, 'example/index.html', context=data)
    #return render(request, 'example/index.html')