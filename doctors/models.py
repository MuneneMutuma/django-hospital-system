from django.db import models
from django.contrib.auth.models import User

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    # gender = models.Choices({'Male':'M', 'Female':'F'})
    department = models.CharField(max_length=50)
    age = models.IntegerField(max_length=3)
    # availability = models.TextChoices()
    
    def __str__(self):
        return self.name
    

