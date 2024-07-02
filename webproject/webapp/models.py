from django.db import models

# Create your models here.


class Customer(models.Model):
    cus_name = models.CharField(max_length=100)
    cus_email = models.EmailField()
    cus_phone_number = models.CharField(max_length=15)
    date = models.CharField(max_length=10)
    time = models.CharField(max_length=5)
    number_of_people = models.IntegerField()
    massage = models.TextField()

    class Meta:
        db_table = "tb_customer"
