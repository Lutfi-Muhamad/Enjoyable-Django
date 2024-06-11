from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BASE, name="BASE"),
    path("recipe.html/", views.recipe, name="recipe"),
    path("accounts/login/", views.login, name="login"),
]
