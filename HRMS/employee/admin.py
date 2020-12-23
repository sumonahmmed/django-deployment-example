from django.contrib import admin
from employee.models import BranchDetails, EmployeeInput, Gender, Userprofile

# Register your models here.


class BranchDetailsAdmin(admin.ModelAdmin):
    list_display = ('branch_name', 'branch_code', 'branch_district')


class EmployeeInputAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'employee_gender', 'employee_branch', 'employee_joining_date')


admin.site.register(BranchDetails,BranchDetailsAdmin),
admin.site.register(EmployeeInput, EmployeeInputAdmin),
admin.site.register(Gender),
admin.site.register(Userprofile),