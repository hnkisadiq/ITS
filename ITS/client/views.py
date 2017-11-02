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
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
#from emails.forms import ContactForm
from twilio.rest import Client
from django.conf import settings

import twilio
import twilio.rest

from twilio.rest import TwilioRestClient
from django.conf import settings

from twilio.rest import TwilioRestClient

from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt


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

def fmail(request):
    if request.method == 'POST':
        to_email = request.POST.get['email_id']
        phn_num = request.POST.get['phn_num']
        message = request.POST.get['message']
        subject = "ITS Project"
        from_email = settings.EMAIL_HOST_USER

        try:

            send_mail(subject, message, from_email, ['sunnya40@gmail.com'], fail_silently=False, auth_user=None,
                      auth_password=None, connection=None, html_message=None)

            account_sid = "AC192abda9f903457d965660e194d06440"
            auth_token = "2fdc4f7ce4624083845b6a2660fe80d4"

            client = Client(account_sid, auth_token)

            message = client.messages.create(
                to="+918897987886",
                from_="+12345426740",
                body=message)

            print(message.sid)

        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('thanks')
    return render(request, "index.html")

def thanks(request):
    return HttpResponse('Thank you for your message.')
