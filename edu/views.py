from django.shortcuts import render


def skill(request):
    return render(request, 'edu/skills.html')
