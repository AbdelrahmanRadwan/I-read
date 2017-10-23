from django.contrib import admin
from django.conf.urls import url, include
from accounts.views import ListUserView

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^books/', include('books.urls')),
    url (r'^api/', include("books.api.urls")),
    url(r'^users/', include('accounts.urls')),
]
