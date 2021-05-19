from django.shortcuts import redirect, render

from .models import ContactUs


# Create your views here.

def contactForm(request):
    if request.method == 'POST':
        response = request.POST
        name = response.get('name')
        email = response.get('email')
        website = response.get('website')
        message = response.get('message')
        data = ContactUs(name=name, email=email, website=website, message=message)
        data.save()
    return redirect('contactUs')


def contactList(request):
    if not request.user.is_authenticated:
        return redirect('Login')

    data = ContactUs.objects.all()

    return render(request, 'admin/contactList.html', {'data': data})


def contactDelete(request, pk):
    data = ContactUs.objects.filter(pk=pk)
    data.delete()
    return redirect('contactList')
