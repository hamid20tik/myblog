from django.shortcuts import render
from django.http import HttpResponse

def homepage(requset):
    return render(requset,'jobs/home.html')