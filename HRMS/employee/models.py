from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.


class Userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


class BranchDetails(models.Model):
    branch_name = models.CharField(verbose_name='Branch Name', max_length=255)
    branch_code = models.CharField(verbose_name='Branch Code', max_length=10)
    branch_licence_no = models.CharField(verbose_name='Branch Licence No', max_length=255)
    branch_district = models.CharField(verbose_name='Branch District', max_length=255)
    branch_opening_date = models.DateField(verbose_name='Branch Opening Date', default=timezone.now())

    def __str__(self):
        return self.branch_name


class Gender(models.Model):
    gender_type = models.CharField(max_length=255)

    def __str__(self):
        return self.gender_type


class EmployeeInput(models.Model):
    employee_name = models.CharField(verbose_name='Name', max_length=255)
    employees_father_name = models.CharField(verbose_name='Father Name', max_length=255)
    employee_mother_name = models.CharField(verbose_name='Mother Name', max_length=255)
    employee_date_of_birth = models.DateField(verbose_name='Date of Birth')
    employee_gender = models.ForeignKey(Gender, on_delete=models.CASCADE, verbose_name='Gender')
    employee_nid = models.CharField(verbose_name='NID', max_length=25)
    employee_birth_registration_no = models.CharField(verbose_name='Birth Registration Number', max_length=50,
                                                      null=True, blank=True)
    employee_tin_no = models.CharField(verbose_name='TIN Number', max_length=30, null=True, blank=True)
    employee_mobile_number = models.CharField(verbose_name='Mobile Number', max_length=15)
    employee_email = models.EmailField(verbose_name='Email')
    employee_present_address = models.TextField(verbose_name='Present Address', max_length=2500)
    employee_permanent_address = models.TextField(verbose_name='Permanent Address', max_length=2500)
    employee_branch = models.ForeignKey(BranchDetails, on_delete=models.CASCADE, verbose_name='Branch Name')
    employee_joining_date = models.DateField(verbose_name='Date of Joining')