
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^pollsapp/', include('pollsapp.urls')),
    url(r'^admin/', admin.site.urls),
]
