
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^books/', include('books.urls')),
    url (r'^api/', include("books.api.urls"))
]
