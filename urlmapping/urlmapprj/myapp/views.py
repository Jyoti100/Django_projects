from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import time

def hello(request):
    text='<h1>Hello app </h1>'
    text += '<br><h1>I am practicing Url mapping in django</h1>'
    return HttpResponse(text)

def morning(request):
    return render(request,'morning.html', {})

def article(request, id):
    text='<h1>displaying article details: %s</h1>'%id
    return HttpResponse(text)

def article1(request, year, month):
    text1='<h3>displaying month and year details: %s/%s</h3>'%(month, year)
    return HttpResponse(text1)

def date(request):
    time1=time.ctime()
    text2="Current time is:%s"%(time1)
    return HttpResponse(text2)

def number(request, i):
    text3='entered number is:' + str(i)
    return HttpResponse(text3)

def year(request, m, y):
    text4 = 'entered year is: %s/%s'%(m, y)
    return HttpResponse(text4)