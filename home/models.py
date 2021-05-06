from django.db import models

# Create your models here.

class BmiMeasurement(models.Model):
    STATUS_CHOICES = (
        ("underweight", "UNDERWEIGHT"), 
        ("normal", "NORMAL"), 
        ("overweight", "OVERWEIGHT"), 
        ("obese", "OBESE")
        )
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField(null=True)
    message = models.CharField(max_length=255, choices=STATUS_CHOICES, null=True)

    def __str__(self):
        return self.name
