from django.contrib import admin
from .models import Patient, Insurance, MedicalRecord

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
  model = Patient
  list_display = ['first_name']

class InsuranceAdmin(admin.ModelAdmin):
  model = Insurance
  list_display = ['provider']
class MedicalRecordAdmin(admin.ModelAdmin):
  model = MedicalRecord
  list_display = ['diagnosis', 'date', 'treatment']


admin.site.register(Patient, PatientAdmin)
admin.site.register(Insurance, InsuranceAdmin)
admin.site.register(MedicalRecord, MedicalRecordAdmin)
