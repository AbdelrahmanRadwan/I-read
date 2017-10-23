from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
from django.conf.urls import url, include
from . import views

app_name = 'books'
urlpatterns = [

    url(r'^create/$', views.CreateBookView),
    url(r'^$', views.ListBookView),
    url(r'^all-books/$', views.ListBookView),

    url(r'^(?P<id>\d+)/$', views.DetailsBookView),
    url(r'^(?P<id>\d+)/edit/$', views.UpdateBookView),
    url(r'^(?P<id>\d+)/delete/$', views.DeleteBookView),

]