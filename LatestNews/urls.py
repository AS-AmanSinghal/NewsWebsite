from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^news/(?P<name>.*)/$', views.NewsDetail, name='NewsDetail'),
    url(r'^panel/addnews/$', views.addNews, name='AddNews'),
    url(r'^panel/newsDelete/(?P<pk>\d+)/$', views.newsDelete, name='newsDelete')
]
