
from django.contrib import admin
from django.conf.urls import url, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^blog/', include('blog.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^cadmin/', include('cadmin.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
