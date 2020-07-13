from django.db import models

# Create your models here.
class Friends(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    first_met = models.CharField(max_length=100)
    home_town = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    createddate = models.DateTimeField(auto_now_add=True, null=True)
    updateddate = models.DateTimeField(auto_now=True, null=True)
