from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^login', views.login, name='login'),
    url(r'^secret', views.secret, name='secret'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^test_session/', views.test_session, name='test_session'),
    url(r'^test_delete/', views.test_delete, name='test_delete'),
    url(r'^cookie/', views.test_cookie, name='cookie'),
    # url(r'^trackuser/', views.track_user, name='track_user'),
    url(r'/stop_tracking', views.stop_tracking, name='stop_tracking'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.post_by_category, name='post_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.post_by_tag, name='post_by_tag'),
    url(r'^(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'^$', views.post_list, name='post_list'),
    url(r'^blog/$', views.test_redirect, name='test_redirect'),

]