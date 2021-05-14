from django.shortcuts import render

from .models import NewsAppModel


# Create your views here.

def home(request):
    # siteName = NewsAppModel.objects.filter(pk=2)
    siteName = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/home.html', {'site': siteName})


def about(request):
    # siteName = NewsAppModel.objects.filter(pk=2)
    siteName = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/about.html', {'site': siteName})
