from django.shortcuts import render, redirect

from newsApp.models import NewsAppModel
from .models import LatestNews


# Create your views here.


def NewsDetail(request, name):
    news = LatestNews.objects.get(name=name)
    site = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/news_detail.html', {'site': site, 'news': news})


def addNews(request):
    if request.method == 'POST':
        response = request.POST
        data = LatestNews(name=response.get('name'), short_text=response.get('short_text'),
                          description=response.get('description'), date=response.get('date'),
                          image=response.get('image'), writer=response.get('writer'))
        data.save()
        return redirect('AddNews')

    return render(request, 'admin/addnews.html')
