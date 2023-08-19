from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name = "Apinun"
    age = 24
    return render(request, "index.html", {"age": age, "name": name})

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")