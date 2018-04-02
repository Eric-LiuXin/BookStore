from django.shortcuts import render
from django.template.loader import get_template
from .models import Books
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    template = get_template('index.html')
    books = Books.objects.all()[0:3]

    html = template.render(locals())

    return HttpResponse(html)

def shelf(request):
    template = get_template('shelf.html')
    books = Books.objects.all()

    html = template.render(locals())

    return HttpResponse(html)

def user(request):
    template = get_template('user.html')

    html = template.render(locals())

    return HttpResponse(html)