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

def well(request):
    depth = request.GET['k']
    return render(request,'3d.html?k='+depth+'')

def test(request):
    url1 = 'http://10.0.3.23:8076/farm/'
    url2 = 'http://10.0.3.23:8076/house/'
    url3 = 'http://10.0.3.23:8076/well/'
    url4 = 'http://10.0.3.23:8076/crop/'
    response1 = urllib.urlopen(url1)
    response2 = urllib.urlopen(url2)
    response3 = urllib.urlopen(url3)
    response4 = urllib.urlopen(url4)
    js_data1 = json.loads(response1.read())
    js_data2 = json.loads(response2.read())
    js_data3 = json.loads(response3.read())
    js_data4 = json.loads(response4.read())
    return render(request,'index.html', {"farm": js_data1,"house": js_data2,"well":js_data3,"crop":js_data4})

