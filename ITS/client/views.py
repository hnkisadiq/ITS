# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template import loader
#from .models import Question
from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
import urllib
#from django.utils import simplejson
# Create your views here.
def data(request):
    url = 'http://PaiSan6556.pythonanywhere.com/identity'
    response = urllib.urlopen(url)
    r = json.loads(response.read())
    return HttpResponse(r)

def data2(request):
    url = 'http://PaiSan6556.pythonanywhere.com/farm'
    response = urllib.urlopen(url)
    r = json.loads(response.read())
    return HttpResponse(r)

def data3(request):
    url = 'http://Paisan6556.pythonanywhere.com/house'
    response = urllib.urlopen(url)
    r = json.loads(response.read())
    return HttpResponse(r)

def test(request):
    url1 = 'http://10.0.3.23:8076/farm/'
    url2 = 'http://10.0.3.23:8076/house/'
    response1 = urllib.urlopen(url1)
    response2 = urllib.urlopen(url2)
    js_data1 = json.loads(response1.read())
    js_data2 = json.loads(response2.read())
    return render(request,'index.html', {"farm": js_data1,"house": js_data2})

