from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
     STATUS_CHOICES = (
         ("male","MALE"), 
         ("female", "FEMALE"), 
         ("other", "OTHER")
         )
     user = models.OneToOneField(User, on_delete=models.CASCADE)    
    #  name = models.CharField(max_length=255)
     age = models.FloatField()
     gender = models.CharField(max_length=255,choices=STATUS_CHOICES)
     contact = models.CharField(max_length=255)
     address = models.CharField(max_length=255)

     def __str__(self):
         return str(self.user)
