from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^panel/subcategory/$', views.subcategory, name='subcategory'),
    url(r'^panel/addSubCategory/$', views.addSubCategory, name='addSubCategory')
]
