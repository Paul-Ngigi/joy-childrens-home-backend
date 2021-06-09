from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
gender_choices = [
    ("Male", 'Male'),
    ("Female", 'Female'),
    ("Other", "Other")
]

marital_status = [
    ("Married", "Married"),
    ("Single", "Single"),
    ("Divorced", "Divorced"),
]


class Adopter(models.Model):
    passport_image = CloudinaryField(blank=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    gender = models.CharField(max_length=10, blank=False, choices=gender_choices, default="Male")
    email = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=12, blank=False)
    id_number = models.CharField(max_length=8, blank=False)
    location = models.CharField(max_length=100, blank=False)
    marital_status = models.CharField(max_length=10, blank=False, choices=marital_status, default="Single")

    def __str__(self):
        return self.first_name
