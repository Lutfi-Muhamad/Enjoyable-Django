from django.shortcuts import render


# Create your views here.
def BASE(request):
    return render(request, "base.html")


def recipe(request):
    return render(request, "recipe.html")


def login(request):
    return render(request, "login.html")
