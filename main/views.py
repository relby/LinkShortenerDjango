from django import shortcuts
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from .forms import CreateLink
from .models import Links
import hashlib

# Create your views here.
def home(response):
    if response.method == "POST":
        form = CreateLink(response.POST)
        if form.is_valid():
            shortened_url = hashlib.sha1(str(response.POST["url"]).encode()).hexdigest()[:7]
            if not Links.objects.filter(shortened_url=shortened_url):
                t = Links(url=response.POST["url"], shortened_url=shortened_url)
                t.save()
        return render(response, "main/home.html", {"form":form, "shortened_url":shortened_url})
    else:
        form = CreateLink()
        return render(response, "main/home.html", {"form":form, "shortened_url":""})

def link(response, sha):
    if Links.objects.filter(shortened_url=sha):
        to_redirect = Links.objects.get(shortened_url=sha).url
        return redirect(to_redirect)
    return redirect(home)