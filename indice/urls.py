from django.urls import path, include
from . import views

from django.contrib.auth.views import login_required,logout_then_login
#from django.contrib.auth.views import login_required,logout_then_login

urlpatterns = [
    #path('', login_required(views.home)),
    path('item', views.item, name='item'),
    ]
