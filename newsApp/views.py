from django.shortcuts import render

from LatestNews.models import LatestNews
from .models import NewsAppModel


# Create your views here.

def home(request):
    # siteName = NewsAppModel.objects.filter(pk=2)
    siteName = NewsAppModel.objects.get(pk=1)
    news = LatestNews.objects.all()

    return render(request, 'frontend/home.html', {'site': siteName, 'latestNews': news})


def about(request):
    # siteName = NewsAppModel.objects.filter(pk=2)
    siteName = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/about.html', {'site': siteName})


def panel(request):
    return render(request, 'admin/home.html')


def newsList(request):
    news = LatestNews.objects.all()
    return render(request, 'admin/newsList.html', {'newsData': news})
