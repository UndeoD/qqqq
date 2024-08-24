from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories

def index(request):

    context = {
        'title': 'Home - Main page',
        'content': 'Showcase',
    }

    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'About us',
        'content': 'About us',
        'text_on_page': "1. you're not a clown. just because you put a gul on your ava, spam zxczczxczcxczcxczcxzxzxc, pause after every kill for no reason and are just a poser - that doesn't mean you're a gul and you have no right to call yourself one.",

    }

    return render(request, 'main/about.html', context)
