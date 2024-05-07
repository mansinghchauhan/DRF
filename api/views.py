from django.shortcuts import render
from rest_framework import viewsets, status
from api.models import Company, Employee
from api.serializers import Company_Serializer, Employee_Serializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.


class CompanyViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = Company_Serializer

    @action(detail=True, methods=["get"])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = Employee_Serializer(
                emps, many=True, context={'request': request})
            if emps:
                return Response(emps_serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'No employees found for this company'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            print(e)
            return Response({
                'message': "company not exists"
            })


class EmployeeViewset(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = Employee_Serializer
