from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^panel/managers/$', views.manageUsers, name='managers'),
    url(r'panel/manager/(?P<pk>\d+)/$', views.managerDelete, name='managerDelete')
]
