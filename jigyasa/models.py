from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# create models for contact to stored the request for the contact

class Contact(models.Model):
    name = models.CharField(max_length=20)
    surname=models.CharField(max_length=30)
    email = models.EmailField(max_length=75)
    phone = PhoneNumberField()
    created_on = models.DateTimeField(auto_now_add=True)