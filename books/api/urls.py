from django.conf.urls import url, include
from . import views
from .views import (
    BookListAPIView,
    BookDetailAPIView,
    BookDeleteAPIView,
    BookUpdateAPIView,
    BookCreateAPIView,
)
app_name = 'books'
urlpatterns = [

url(r'^$', BookListAPIView.as_view()),
url(r'^books/$', BookListAPIView.as_view()),
url(r'^books/create/$', BookCreateAPIView.as_view()),
url(r'^books/create/$', BookCreateAPIView.as_view()),

url(r'^books/(?P<pk>\d+)/$',BookDetailAPIView.as_view() ),
url(r'^books/(?P<pk>\d+/edit)/$',BookUpdateAPIView.as_view() ),
url(r'^books/(?P<pk>\d+/delete)/$',BookDeleteAPIView.as_view() ),


]