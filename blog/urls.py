from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('',views.index,name='index'),  
    path('another/',views.index,name='another'),  
]