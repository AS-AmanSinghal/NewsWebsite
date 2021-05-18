import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from category.models import Category
from newsApp.models import NewsAppModel
from subcategory.models import SubCategory
from .models import LatestNews


# Create your views here.


def NewsDetail(request, name):
    siteName = NewsAppModel.objects.get(pk=1)
    category = Category.objects.all()
    subcategory = SubCategory.objects.all()
    news = LatestNews.objects.all().order_by('-pk')

    showNews = LatestNews.objects.get(name=name)

    return render(request, 'frontend/news_detail.html',
                  {'site': siteName, 'latestNews': news, 'news': showNews, 'category': category
                      , 'subcategory': subcategory})


def addNews(request):
    print("-------------------")
    now = datetime.datetime.now()

    print()
    if request.method == 'POST':
        response = request.POST

        image = request.FILES['image']
        fileSystem = FileSystemStorage()

        if str(image.content_type).startswith('image'):
            if image.size < 20000000:
                fileName = fileSystem.save(image.name, image)
                url = fileSystem.url(fileName)
                data = LatestNews(name=response.get('name'), short_text=response.get('short_text'),
                                  description=response.get('description'), date=response.get('date'),
                                  image=url, writer=response.get('writer'), imageName=fileName)

                data.save()
            else:
                print("SIZE ERROR")
        else:
            print("ERROR")
        return redirect('AddNews')

    return render(request, 'admin/addnews.html')


def newsDelete(request, pk):
    data = LatestNews.objects.get(pk=pk)
    fs = FileSystemStorage()
    fs.delete(data.imageName)
    data.delete()
    return redirect('newsList')


def newsEdit(request, pk):
    data = LatestNews.objects.get(pk=pk)

    if request.method == 'POST':
        response = request.POST
        latesNews = LatestNews.objects.get(pk=pk)
        latesNews.name = response.get('name')
        latesNews.short_text = response.get('short_text')
        latesNews.description = response.get('description')
        latesNews.date = response.get('date')
        latesNews.writer = response.get('writer')
        latesNews.save()
        return redirect('newsList')
    return render(request, 'admin/addnews.html', {'newsData': data})
