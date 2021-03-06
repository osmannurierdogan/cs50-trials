from django.urls import path

from . import views

app_name = "tasks"
urlpatterns = [
    path("home", views.index, name = "index"),
    path("add", views.add, name = "add")
]