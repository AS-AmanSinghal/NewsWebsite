from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^news/(?P<name>.*)/$', views.NewsDetail, name='NewsDetail')
]
