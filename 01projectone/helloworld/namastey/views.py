from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def namasteyPageView(request):
    return HttpResponse('Namastey mean hello in Hindi')
