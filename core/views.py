from django.shortcuts import render
from .models import customerData
from .forms import InquiryForm


def home(request):
    context = {
        'home': 'active'
    }
    return render(request, 'core/home.html', context)


def contact(request):
    if request.method == 'POST':
        # Using forms.py
        fm = InquiryForm(request.POST)

        if fm.is_valid():
            name = fm.cleaned_data['inputName']
            email = fm.cleaned_data['inputEmail']
            subject = fm.cleaned_data['inputSubject']
            message = fm.cleaned_data['inputMessage']
            print(name, email, message, subject)
            data = customerData(name=name, email=email,
                                subject=subject, message=message)
            data.save()
            context = {
                'contact': 'active',
                'name': name,
            }
            return render(request, 'core/success.html', context)

    else:
        fm = InquiryForm()
    context = {
        'contact': 'active',
        'form': fm
    }
    return render(request, 'core/contact.html', context)
