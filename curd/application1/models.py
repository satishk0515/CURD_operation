from django.db import models

# Create your models here.

class user(models.Model):
    Name=models.CharField(max_length=70)
    Email=models.EmailField(max_length=50)
    Password=models.CharField(max_length=30)
    