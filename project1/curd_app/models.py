from django.db import models


class Company(models.Model):
    PAYMENT_CHOICE = [("OFF", "Offline"), ("OL", "Online")]
    CITY_CHOICE = [("PUNE", "Pune"), ("NASHIK", "Nashik"), ("MUMBAI", "Mumbai")]
    company_name = models.CharField(max_length=20)
    company_owner = models.CharField(max_length=20)
    total_emp = models.IntegerField()
    city_pincode = models.IntegerField()
    payment_mode = models.CharField(max_length=20, choices=PAYMENT_CHOICE)
    city_mode = models.CharField(max_length=20, choices=CITY_CHOICE, default="Pune")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
