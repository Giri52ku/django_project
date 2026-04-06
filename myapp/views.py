from django.shortcuts import render
from django.http import HttpResponse

from .models import Person

# Create your views here.

def home(request):
    persons = Person.objects.all()
    context = {'persons': persons}
    return render(request, 'index.html',context)