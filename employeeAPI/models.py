from django.db import models


class Employee(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    fullName = models.CharField(max_length=100)
    empCode = models.CharField(max_length=5)
    mobile = models.CharField(max_length=10, unique=True)
    createdDate = models.DateTimeField(auto_now_add=True, null=True)
    updatedDate = models.DateTimeField(auto_now_add=True, null=True)
