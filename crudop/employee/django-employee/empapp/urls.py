from django.conf.urls import url, include
from . import views, views1
#from . import views
urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^signup/', views.signup, name='signup'),

    # Class base view
     url(r'^detail/(?P<pk>\d+)/', views1.EmpDetailView.as_view(), name='detail'),
     url(r'^emp/', views1.EmployeeAddView.as_view(), name='emp'),
     url(r'^show/', views1.ShowView.as_view(), name='show'),
     url(r'^update/(?P<pk>\d+)/$', views1.EmpUpdateView.as_view(), name='update'),
     url(r'^delete/(?P<pk>\d+)/$', views1.EmpDeleteView.as_view(), name='delete'),

    # Function based view
    #  url(r'^detail/(?P<pk>\d+)/', views.detail, name='detail'),
    #  url(r'^emp/', views.emp, name='emp'),
    #  url(r'^show/', views.show, name='show'),
    #  url(r'^update/(?P<pk>\d+)/$', views.update, name='update'),
    #  url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]