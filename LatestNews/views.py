from django.shortcuts import render

from newsApp.models import NewsAppModel
from .models import LatestNews


# Create your views here.


def NewsDetail(request, name):
    news = LatestNews.objects.get(name=name)
    site = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/news_detail.html', {'site': site, 'news': news})
