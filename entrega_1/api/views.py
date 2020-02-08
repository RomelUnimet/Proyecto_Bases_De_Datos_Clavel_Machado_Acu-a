from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(('GET',))
def api_detail(request):
    emp=Employee.objects.all()

    #print(emp)

    serializer=EmployeeSerializer(emp, many=True)

    return Response(serializer.data)