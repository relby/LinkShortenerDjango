from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:sha>", views.link, name="link")
]