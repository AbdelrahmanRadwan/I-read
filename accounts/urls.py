from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls import url, include
from . import views

urlpatterns = [

    url(r'^register/$', views.UserFormView.as_view(), name="Register_"),
    # Local_Host/Home/Login_User/
    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^$', views.ListUserView),
    url(r'^all-users/$', views.ListUserView),
]