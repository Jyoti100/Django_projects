
from django.contrib import admin
from django.conf.urls import url, include

urlpatterns = [
    url(r'^poll/', include('poll.urls')),
    url(r'admin/', admin.site.urls),
]
