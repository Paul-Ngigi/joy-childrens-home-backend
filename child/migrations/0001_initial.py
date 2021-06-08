# Generated by Django 3.2.4 on 2021-06-08 20:38

from django.db import migrations, models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_image', pyuploadcare.dj.models.ImageField(blank=True)),
                ('first_name', models.CharField(max_length=30)),
                ('middle_name', models.CharField(max_length=30)),
                ('surname', models.CharField(blank=True, max_length=30)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('talent', models.CharField(max_length=30)),
                ('medical_records', pyuploadcare.dj.models.FileField(blank=True)),
                ('school_report', pyuploadcare.dj.models.FileField(blank=True)),
            ],
        ),
    ]