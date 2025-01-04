from django.db import models

# Create your models here.


class Patient(models.Model):
  first_name= models.CharField(max_length=200, verbose_name='Name')
  last_name= models.CharField(max_length=200, verbose_name='Last Name')
  date_of_birth = models.DateField(verbose_name='Birth Date')
  contact_number = models.CharField(max_length=20, verbose_name='Number')
  email = models.EmailField(verbose_name='E-mail')

  def __str__(self):
    return f'{self.first_name} {self.last_name}'

class Insurance(models.Model):
  patient = models.ForeignKey(Patient,related_name='insurances',on_delete=models.CASCADE)
  provider = models.CharField(max_length=100, verbose_name='Provider')
  policy_number = models.CharField(max_length=100, verbose_name='Policy Number')
  expiration_date = models.DateField(verbose_name='Expiration Date')

  def __str__(self):
    return f'{self.provider}'

class MedicalRecord(models.Model):
  patient = models.ForeignKey(Patient, related_name='medical_records', on_delete=models.CASCADE)
  date = models.DateField(verbose_name='Date')
  diagnosis = models.TextField(verbose_name='Diagnosis')
  treatment = models.TextField(verbose_name='Treatment')
  follow_up_date = models.DateField(verbose_name='Follow Up Date')
