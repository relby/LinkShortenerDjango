from django.http import HttpResponse
from django.shortcuts import render
from .forms import CreateLink

# Create your views here.
def home(response):
    if response.method == "POST":
        form = CreateLink(response.POST)
    else:
        form = CreateLink()
    return render(response, "main/home.html", {"form":form})