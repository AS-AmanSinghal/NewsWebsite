"""NewsWebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from NewsWebsite.settings import STATIC_ROOT, MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('newsApp.urls')),
    url(r'', include('LatestNews.urls')),
    url(r'', include('category.urls')),
    url(r'', include('subcategory.urls')),
    url(r'', include('contactUs.urls')),
    url(r'', include('manageUsers.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=MEDIA_ROOT)
