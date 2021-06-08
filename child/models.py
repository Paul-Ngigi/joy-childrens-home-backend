from django.db import models
from pyuploadcare.dj.models import ImageField, FileField


# Create your models here.
class Child(models.Model):
    passport_image = ImageField(blank=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30, blank=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    talent = models.CharField(max_length=30, blank=True)
    medical_records = FileField(blank=True)
    school_report = FileField(blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return {self.first_name}
