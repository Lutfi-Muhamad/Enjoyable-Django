from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Customer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def BASE(request):
    return render(request, "base.html")


def recipe(request):
    return render(request, "recipe.html")


def login(request):
    return render(request, "login.html")


def crud(request):
    customer = Customer.objects.all()
    return render(request, "crud.html", {"customer": customer})


def book_a_table(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        people = request.POST.get("people")
        message = request.POST.get("message")

        # Simpan data ke database
        customer = Customer(
            cus_name=name,
            cus_email=email,
            cus_phone_number=phone,
            date=date,
            time=time,
            number_of_people=people,
            massage=message,
        )
        customer.save()
        return HttpResponse(
            "Your booking request was sent. We will call back or send an Email to confirm your reservation. Thank you!"
        )
    return HttpResponse("Error: Invalid request method", status=400)


def add(request):
    return render(request, "crud.html#addEmployeeModal")


def addrecord(request):
    name = request.POST["name"]
    email = request.POST["email"]
    phone = request.POST["phone"]
    date = request.POST["date"]
    time = request.POST["time"]
    people = request.POST["people"]
    message = request.POST["message"]
    customer = Customer(
        cus_name=name,
        cus_email=email,
        cus_phone_number=phone,
        date=date,
        time=time,
        number_of_people=people,
        massage=message,
    )
    customer.save()
    return redirect("crud")


def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect("crud")


def update(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, "update.html", {"customer": customer})


def update_view(request, id):
    customer = get_object_or_404(Customer, id=id)
    if request.method == "POST":
        # Logika untuk memperbarui customer, jika diperlukan
        customer.cus_name = request.POST.get("name")
        customer.cus_email = request.POST.get("email")
        customer.cus_phone_number = request.POST.get("phone")
        customer.date = request.POST.get("date")
        customer.time = request.POST.get("time")
        customer.number_of_people = request.POST.get("people")
        customer.save()
        # Redirect atau memberikan respons yang sesuai
        return redirect("crud")
    return render(request, "update.html", {"customer": customer})
