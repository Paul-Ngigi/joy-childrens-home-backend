from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField

# Create your models here.
User = get_user_model()

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


class Staff(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profile_photo = CloudinaryField('staff', blank=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=gender_choices, default='Female')
    marital_status = models.CharField(max_length=10, choices=marital_status, default='Single')

    def __str__(self):
        return self.user.username
