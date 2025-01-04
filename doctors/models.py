from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    biography = models.TextField()
    department = models.ForeignKey(Department, related_name='doctors', on_delete=models.SET_NULL, null=True)


class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(
        Doctor, related_name='availabilities', on_delete=models.CASCADE
    )
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()