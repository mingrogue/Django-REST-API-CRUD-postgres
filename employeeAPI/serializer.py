from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class UpdateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['fullName', 'empCode', 'mobile', 'updatedDate']
