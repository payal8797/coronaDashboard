from django.db import models

# Create your models here.

class form(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.CharField(max_length=50, default='SOME STRING')
    country = models.CharField(max_length=50)  
    subject = models.TextField()
    