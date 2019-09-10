from django.db import models

# Create your models here.

class User(models.Model):
    First_name = models.CharField(max_length=50)
    Last_name = models.CharField(max_length=50)
    Your_pic = models.ImageField(upload_to='images/')
    Your_details = models.TextField()