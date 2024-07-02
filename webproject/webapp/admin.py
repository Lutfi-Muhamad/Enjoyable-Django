from django.contrib import admin
from .models import Customer


class CustomerMember(admin.ModelAdmin):
    list_display = (
        "cus_name",
        "cus_email",
        "cus_phone_number",
        "date",
        "time",
        "number_of_people",
        "massage",
    )


admin.site.register(Customer, CustomerMember)
