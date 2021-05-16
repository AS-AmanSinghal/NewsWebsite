from django.shortcuts import render, redirect

from .models import Category


# Create your views here.

def category(request):
    categoryData = Category.objects.all()
    return render(request, 'admin/category/category.html', {'categoryData': categoryData})


def addCategory(request):
    if request.method == 'POST':
        if request.POST.get('name') != None:
            if len(Category.objects.filter(category=request.POST.get('name'))) == 0:
                data = Category(category=request.POST.get('name'))
                data.save()
                return redirect('addCategory')

    return render(request, 'admin/category/addCategory.html')


def deleteCategory(request, pk):
    data = Category.objects.get(pk=pk)
    data.delete()
    return redirect('category')
