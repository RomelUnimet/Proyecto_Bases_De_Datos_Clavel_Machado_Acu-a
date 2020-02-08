from .models import Employee
from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields= '__all__'
        fields= ['id','ci','name', 'last_name', 'phone', 'points', 'adress', 'gender', 'birth_date', 'job_id', 'is_active']



   