from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^contactForm/$', views.contactForm, name='contactForm'),
    url(r'^panel/contact/$', views.contactList, name='contactList'),
    url(r'^panel/contactDelete/(?P<pk>\d+)/$', views.contactDelete, name='contactDelete')
]
