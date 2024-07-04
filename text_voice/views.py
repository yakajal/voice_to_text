from django.shortcuts import render

# Create your views here.

import pyttsx3

def converter(request):
    text=pyttsx3.init()
    name=request.POST.get('name')
    text.setProperty('volume',0.9)
    text.say(name)
    return render(request,'next.html',text.runAndWait())