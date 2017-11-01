from django.conf.urls import url

from client import views

urlpatterns = [
url(r'^test/$', views.test, name='test'),
    url(r'^test/3d.html/$', views.well, name='3d'),
]

