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
    fm = InquiryForm()
    context = {
        'contact': 'active',
        'form': fm
    }
    return render(request, 'core/contact.html', context)


# def saveCustomerData(request):
    if request.method == 'POST':
        # name = request.POST.get('inputName')
        # email = request.POST.get('inputEmail')
        # subject = request.POST.get('inputSubject')
        # message = request.POST.get('inputTextarea')
        # data = customerData(name=name, email=email,
        #                     subject=subject, message=message)
        # data.save()
        fm = InquiryForm(request.POST)
        # Using forms.py
        if fm.is_valid():
            name = fm.cleaned_data['inputName']
            email = fm.cleaned_data['inputEmail']
            subject = fm.cleaned_data['inputSubject']
            message = fm.cleaned_data['inputTextarea']
            data = customerData(name=name, email=email,
                                subject=subject, message=message)
            data.save()
    else:
        fm = InquiryForm()
    context = {
        'contact': 'active',
        'form': fm
    }
    return render(request, 'core/contact.html', context)
