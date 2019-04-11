from django.shortcuts import render
from django.http import HttpResponse
from .models import job
def homepage(requset):
    jobs = job.objects
    return render(requset,'jobs/home.html',{'jobs':jobs})