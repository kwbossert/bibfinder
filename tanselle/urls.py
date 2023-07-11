from django.urls import path
from tanselle import views

urlpatterns = [
    path("", views.home, name="home"),
]