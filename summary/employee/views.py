from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
def get_employees(request):
    employee_obj = Employee.objects.all()

    employee_obj_serialized = EmployeeSerializer(employee_obj, many=True).data

    return Response(employee_obj_serialized, status=HTTP_200_OK)


# Create your views here.
