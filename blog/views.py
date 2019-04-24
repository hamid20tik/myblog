from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import blog

def blogi(request):
    blogall=blog.objects
    return render(request,'blog/allblog.html',{'blogall':blogall})

def detailb(request, blog_id):
    detailblog=get_object_or_404(blog, pk=blog_id)
    return render(request,'blog/detail.html',{'dblog':detailblog})