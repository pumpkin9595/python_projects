from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    html = "Rango says hey there partner!"
    return HttpResponse(html)