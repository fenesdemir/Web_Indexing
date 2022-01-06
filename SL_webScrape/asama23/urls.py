from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="a23-home"),
]