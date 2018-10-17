from django.urls import path
from . import views

urlpatterns = [
    path('', views.namasteyPageView, name='namastey'),
    
]