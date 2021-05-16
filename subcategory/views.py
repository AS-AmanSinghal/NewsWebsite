from django.shortcuts import render, redirect

from category.models import Category
from .models import SubCategory


# Create your views here.

def subcategory(request):
    data = SubCategory.objects.all()
    return render(request, 'admin/subcategory/subcategorylist.html', {'subCategoryData': data})


def addSubCategory(request):
    categoryData = Category.objects.all()

    if request.method == 'POST':
        category_id = request.POST.get('category_id')
        subcategory = request.POST.get('subcategory')

        if len(SubCategory.objects.filter(subcategory=subcategory)) == 0:
            category = Category.objects.get(pk=category_id)
            data = SubCategory(category=category, category_id=category_id, subcategory=subcategory)
            data.save()
            return redirect('addSubCategory')

    return render(request, 'admin/subcategory/addSubcategory.html', {'categoryData': categoryData})
