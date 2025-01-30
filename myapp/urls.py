from django.urls import path

from . import views

urlpatterns = [
    path("", views.summary, name="summary"),
    path("list", views.list, name="list"),
    path("add_person", views.PersonCreateView.as_view(), name="add_person")
]