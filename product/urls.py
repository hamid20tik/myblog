from django.urls import path
from . import views
urlpatterns = [
    path('phome/',views.product_home,name='phome'),
    path('create/',views.create,name='create'),
    path('<int:product_id>',views.detailp,name='detailp'),
    path('<int:product_id>/upvote',views.upvote,name='upvote'),
]
