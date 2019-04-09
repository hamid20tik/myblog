
from django.http import HttpResponse
from django.shortcuts import render

def homepage(requset):
    return render(requset,'jobs/home.html',)