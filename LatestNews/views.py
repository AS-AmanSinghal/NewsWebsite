import datetime

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect

from newsApp.models import NewsAppModel
from .models import LatestNews


# Create your views here.


def NewsDetail(request, name):
    news = LatestNews.objects.get(name=name)
    site = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/news_detail.html', {'site': site, 'news': news})


def addNews(request):
    print("-------------------")
    now = datetime.datetime.now()

    print()
    if request.method == 'POST':
        response = request.POST

        image = request.FILES['image']
        fileSystem = FileSystemStorage()

        if str(image.content_type).startswith('image'):
            if image.size < 2000:
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
