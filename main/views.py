from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'title': 'Home',
        'content': 'Page content',
        'list': ['first', 'second', 'third'],
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'bool': True
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("about")
