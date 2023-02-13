from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path("",views.login,name='Login'),
   path("anime",views.anime,name='Anime'),
   path("show/<str:name>",views.show,name='Show'),
   
]
