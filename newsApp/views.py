from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from LatestNews.models import LatestNews
from category.models import Category
from subcategory.models import SubCategory
from .models import NewsAppModel


# Create your views here.

def home(request):
    # siteName = NewsAppModel.objects.filter(pk=2)
    siteName = NewsAppModel.objects.get(pk=1)
    news = LatestNews.objects.all().order_by('-pk')

    category = Category.objects.all()
    subcategory = SubCategory.objects.all()

    return render(request, 'frontend/home.html', {'site': siteName, 'latestNews': news, 'category': category
        , 'subcategory': subcategory})


def about(request):
    # siteName = NewsAppModel.objects.filter(pk=2)
    siteName = NewsAppModel.objects.get(pk=1)

    return render(request, 'frontend/about.html', {'site': siteName})


def panel(request):
    # for authenticated (check login)
    if not request.user.is_authenticated:
        return redirect('Login')

    return render(request, 'admin/home.html')


def newsList(request):
    news = LatestNews.objects.all()
    return render(request, 'admin/newsList.html', {'newsData': news})


def loginPage(request):
    if request.method == 'POST':
        response = request.POST
        username = response.get('username')
        password = response.get('password')

        user = authenticate(username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('admin')
    return render(request, 'frontend/login/login.html')


def logoutPage(request):
    logout(request)
    return redirect('Login')

def settingPage(request):
    data = NewsAppModel.objects.get(pk=1)
    if request.method == 'POST':
        response = request.POST
        name = response.get('name')
        about = response.get('about')
        fb = response.get('facebook')
        twitter = response.get('twitter')
        youtube = response.get('youtube')
        contactNumber = response.get('mobile_number')

        data = NewsAppModel.objects.get(pk=1)
        data.name = name
        data.about = about
        data.fb = fb
        data.twitter = twitter
        data.youtube = youtube
        data.contactNumber = contactNumber
        data.save()
        return redirect('admin')

    return render(request, 'admin/settings.html', {'data': data})
