from django.db import models

# Create your models here.

# Create company mode


class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    about = models.CharField(max_length=200)
    types = models.CharField(max_length=100, choices=(
        ('ID', 'ID'), ('non it', 'not it'), ('mobile', 'phone')))


added_date = models.DateTimeField(auto_now=True)
active = models.BooleanField(default=True)


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    about = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    employee_types = models.CharField(max_length=100, choices=(
        ('manager', 'Manager'), ('hr', 'HR'), ('developer', 'Developer')))
