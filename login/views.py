from django.shortcuts import render, HttpResponseRedirect
from .forms import SignupForm, LoginForm, ChangePasswordForm, ChangePasswordForm1
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
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
            return HttpResponseRedirect('/user/login/')
            # return render(request, 'login/data.html', context)

    else:
        context = {
            'signup': 'active',
            'form': SignupForm(),
        }
    return render(request, 'login/signup.html', context)


# LogIn view function
def log_in(request):
    if not request.user.is_authenticated:
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
                    return HttpResponseRedirect('/user/data/')
    else:
        return HttpResponseRedirect('/user/data/')
    fm = LoginForm()
    context = {
        'signup': 'active',
        'form': LoginForm(),
    }
    return render(request, 'login/login.html', {'form': fm})


def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')


def change_pwd(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ChangePasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('login/data.html')
        else:
            fm = ChangePasswordForm(user=request.user)
        return render(request, 'login/changepwd.html', {'form': fm})
    else:
        return HttpResponseRedirect('/user/login/')


# without old password
def change_pwd1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = ChangePasswordForm1(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('login/data.html')
        else:
            fm = ChangePasswordForm1(user=request.user)
        return render(request, 'login/changepwd.html', {'form': fm})
    else:
        return HttpResponseRedirect('/user/login/')


def data(request):
    if request.user.is_authenticated:
        db = customerData.objects.all()
        return render(request, 'login/data.html', {'data': db})
    else:
        return HttpResponseRedirect('/user/login/')


def deleteData(request, id):
    if request.method == 'POST':
        pi = customerData.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/user/data/')
