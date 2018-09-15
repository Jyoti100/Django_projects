
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^hello/', views.hello, name='hello'),
    url(r'^morning/',views.morning, name='morning'),
    url(r'^(\d{4})/(\d{2})', views.article1, name='article1'),
    url(r'^(\d+)/$', views.article, name='article'),

]