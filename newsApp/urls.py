from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='about'),
    url(r'^panel/$', views.panel, name='admin'),
    url(r'^panel/newsList/$', views.newsList, name='newsList'),
    url(r'^login/$', views.loginPage, name='Login'),
    url(r'^logout/$', views.logoutPage, name='LogOut'),
    url(r'^panel/settings/$', views.settingPage, name='settingPage'),
    url(r'^contact/$', views.contactUs, name='contactUs'),
    url(r'^panel/changepassword/$', views.changePassword, name='changePassword')
]
