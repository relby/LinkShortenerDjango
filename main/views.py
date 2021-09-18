from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "main/home.html", {})

def test(response):
    return render(response, "main/test.html", {})