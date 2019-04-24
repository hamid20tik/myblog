from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.blogi,name='allblog'),
    path('<int:blog_id>/',views.detailb,name='detail'),
]
