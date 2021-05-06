from django.contrib import admin
from home.models import BmiMeasurement

# Register your models here.

@admin.register(BmiMeasurement)
class BmiMeasurementAdmin(admin.ModelAdmin):
    list_display = ("name", "weight", "height", "bmi", "message", )
