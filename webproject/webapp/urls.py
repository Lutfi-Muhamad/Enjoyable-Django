from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.BASE, name="BASE"),
    path("recipe.html/", views.recipe, name="recipe"),
    path("crud.html/", views.crud, name="crud"),
    path("accounts/login/", views.login, name="login"),
    path("book-a-table/", views.book_a_table, name="book-a-table"),
    path("crud.html/addrecord", views.addrecord, name="addrecord"),
    path("crud.html/delete/<int:id>/", views.delete, name="delete"),
    path("update/<int:id>/", views.update, name="update"),
    path("update.html/<int:id>/", views.update_view, name="update"),
]
