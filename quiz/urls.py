from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^result', views.result, name = 'result'),
    url(r'^about', views.about, name = 'about'),
    url(r'^contact', views.contact, name = 'contact'),
    url(r'^(?P<choice>[\w]+)', views.questions, name = 'questions'),
]
