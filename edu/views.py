from django.shortcuts import render


def skill(request):
    context = {
        'skill': 'active'
    }
    return render(request, 'edu/skills.html', context)
