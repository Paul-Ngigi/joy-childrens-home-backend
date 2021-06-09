from django.db import models
from adopter.models import Adopter
from sponser.models import Sponser
from cloudinary.models import CloudinaryField

# Create your models here.
gender_choices = [
    ("Male", 'Male'),
    ("Female", 'Female'),
    ("Other", "Other")
]


class Child(models.Model):
    passport_image = CloudinaryField(blank=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)
    age = models.IntegerField()
    adopter = models.ForeignKey(Adopter, blank=True, null=True, on_delete=models.SET_NULL)
    sponser = models.ForeignKey(Sponser, blank=True, null=True, on_delete=models.SET_NULL)
    gender = models.CharField(max_length=10, choices=gender_choices)
    talent = models.CharField(max_length=30, blank=True)
    medical_records = models.FileField(upload_to="static/medical", blank=True)
    school_report = models.FileField(upload_to="static/school", blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

    def save_child(self):
        self.save()

    def delete_child(self):
        self.delete()
