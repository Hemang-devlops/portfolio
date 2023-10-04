from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from core.models import customerData

# Signup view function


def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            context = {
                'contact': 'active',
                'name': fm.cleaned_data['username'],
            }
            messages.success(request, 'Account created successfully !')
            fm.save()
            return render(request, 'login/data.html', context)

    else:
        context = {
            'signup': 'active',
            'form': SignupForm(),
        }
    return render(request, 'login/signup.html', context)


# LogIn view function
def log_in(request):
    if request.method == 'POST':
        fm = LoginForm(request=request, data=request.POST)
        if fm.is_valid():
            uname = fm.cleaned_data['username']
            upwd = fm.cleaned_data['password']
            user = authenticate(username=uname, password=upwd)
            if user:
                login(request, user)
                context = {
                    'contact': 'active',
                    'name': uname,
                }
                return render(request, 'login/data.html', context)
    else:
        fm = LoginForm()
        context = {
            'signup': 'active',
            'form': LoginForm(),
        }
    return render(request, 'login/login.html', {'form': fm})


def data(request):
    db = customerData.objects.all()
    return render(request, 'login/data.html', {'data': db})


def deleteData(request, id):
    if request.method == 'POST':
        pi = customerData.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/user/data/')
