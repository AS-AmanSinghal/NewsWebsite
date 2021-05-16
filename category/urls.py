from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^panel/category', views.category, name='category'),
    url(r'^panel/addCategory', views.addCategory, name='addCategory'),
    url(r'^panel/deleteCategory/(?P<pk>\d+)/$', views.deleteCategory, name='deleteCategory')
]
