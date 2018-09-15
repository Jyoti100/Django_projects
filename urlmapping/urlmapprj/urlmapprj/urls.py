
from django.contrib import admin
from django.conf.urls import url,include
from myapp import views
from . import view
urlpatterns = [
    #path('admin/', admin.site.urls),
    #url(r'^hello/', views.hello, name='hello'),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^date/', include('myapp.urls1')),
    url(r'^number/(\d+)/', views.number, name='number'),
    url(r'^year/(\d{2})/(\d{4})/', views.year, name='year'),
    url(r'^this/', view.helllo, name='nammeee'),
    url(r'^navapp/', include('navapp.urls')),
    url(r'^admin/', admin.site.urls),

]
