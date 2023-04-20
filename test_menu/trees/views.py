from django.shortcuts import render
from .models import ChieldMenu


def index(request):
    menues = ChieldMenu.objects.filter(father_name=None)
    context = {
        'menues': menues,
    }
    return render(request, 'trees/index.html', context)


def menu(request, id=None):
    context = {
        'id': id,
    }
    return render(request, 'trees/index.html', context)
