from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^welcome/', views.welcome, name='welcome'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
]