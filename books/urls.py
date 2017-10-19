from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r'^create/$', views.CreateBookView),
    url(r'^$', views.ListBookView),
    url(r'^all-books/$', views.ListBookView),
    url(r'^(?P<id>\d+)/$', views.DetailsBookView),
    url(r'^all-authors/$', views.ListAuthorView),

    # Local_Host/Home/
    url(r'^$', views.view_home, name="Home_"),
    # Local_Host/Home/author/123
    url(r'^author/(?P<view_author>[0-9]+)/$', views.view_author, name="Author_"),
    # Local_Host/Home/book/123
    url(r'^book/(?P<view_book>[0-9]+)/$', views.view_book, name="Book_"),
    # Local_Host/Book_ID/favourite

]