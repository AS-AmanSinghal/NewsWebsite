from django.shortcuts import redirect

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
