from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^name/$', views.article_by_name, name='article_by_name'),

    # Class based url
    url(r'^(?P<slug>[-\w]+)/$', views.TaskView.as_view(), name='detail'),

    # function based url
    # url(r'^(?P<slug>[-\w]+)/$', views.article_detail, name='detail'),
    ]