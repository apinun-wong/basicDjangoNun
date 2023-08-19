from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h2>Hello World Django from Nun</h2>")

def about(request):
    return HttpResponse("<h2>About</h2>")

def form(request):
    return HttpResponse("<h2>Form</h2>")