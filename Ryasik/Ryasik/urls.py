from django.urls import path
from Rostislav import views

urlpatterns = [
    path('', views.index),
    path("about/", views.about),
    path("contacts/", views.contacts),
    path("forms/", views.forms),
]
