from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import product
from django.utils import timezone
@login_required()
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            prod = product()
            prod.title = request.POST['title']
            prod.body = request.POST['body']
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                prod.url = request.POST['url']
            else:
                prod.url = 'http://'+ request.POST['url']
            prod.image = request.FILES['image']
            prod.icon = request.FILES['icon']
            prod.pub_date = timezone.datetime.now()
            prod.hunter = request.user
            prod.save()
            return redirect('/product/' + str(prod.id))
        else:
            return render(request, 'product/create.html',{'error':'هیچ فیلدی نمیتواند خالی باشد'})
    else:
        return render(request,'product/create.html')

def detailp(request,product_id):
    prod=get_object_or_404(product,pk=product_id)
    return render(request,'product/detailp.html',{'prod':prod})

def upvote(request,product_id):
    if request.method == 'POST':
        prod = get_object_or_404(product,pk=product_id)
        prod.votes_total+=1
        prod.save()
        return redirect('/product/' + str(prod.id))
def product_home(request):
    pro = product.objects
    return render(request,'product/product_home.html',{'pro':pro})