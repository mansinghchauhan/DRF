from rest_framework import serializers
from api.models import Company, Employee
# create serializer company


class Company_Serializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['name', 'location', 'company_id']


class Employee_Serializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    employee_id = serializers.ReadOnlyField()

    class Meta:
        model = Employee
        fields = "__all__"
