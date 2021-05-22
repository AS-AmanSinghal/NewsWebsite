from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import ManageUsers


# Create your views here.

def manageUsers(request):
    managerData = ManageUsers.objects.all()
    return render(request, 'admin/manager/manager_list.html', {'managersData': managerData})


def managerDelete(request, pk):
    data = ManageUsers.objects.get(pk=pk)
    username = data.name
    user = User.objects.filter(username=username)
    user.delete()
    data.delete()
    return redirect('managers')
