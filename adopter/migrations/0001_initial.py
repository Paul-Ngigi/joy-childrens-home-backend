# Generated by Django 3.2.4 on 2021-06-09 13:00

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adopter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_image', cloudinary.models.CloudinaryField(blank=True, max_length=255)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Male', max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('phone_number', models.CharField(max_length=12)),
                ('id_number', models.CharField(max_length=8)),
                ('location', models.CharField(max_length=100)),
                ('marital_status', models.CharField(choices=[('Married', 'Married'), ('Single', 'Married'), ('Divorced', 'Married')], default='Single', max_length=10)),
            ],
        ),
    ]
