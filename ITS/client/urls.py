from django.conf.urls import url

from client import views

urlpatterns = [
    url(r'^data/$', views.data, name='data'),
 url(r'^data3/$', views.data3, name='data3'),
 url(r'^data2/$', views.data2, name='data2'),
url(r'^test/$', views.test, name='test'),
]

