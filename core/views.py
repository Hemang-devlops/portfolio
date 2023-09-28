from django.shortcuts import render
from .models import customerData


def home(request):
    context = {
        'home': 'active'
    }
    return render(request, 'core/home.html', context)


def contact(request):
    context = {
        'contact': 'active'
    }
    return render(request, 'core/contact.html', context)


def saveCustomerData(request):
    if request.method == 'POST':
        name = request.POST.get('inputName')
        email = request.POST.get('inputEmail')
        subject = request.POST.get('inputSubject')
        message = request.POST.get('inputTextarea')
        data = customerData(name=name, email=email,
                            subject=subject, message=message)
        data.save()
    context = {
        'contact': 'active'
    }
    return render(request, 'core/contact.html', context)
