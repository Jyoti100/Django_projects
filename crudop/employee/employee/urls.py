
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^empapp/', include('empapp.urls')),
    url(r'admin/', admin.site.urls),
]
