from django.contrib import admin
from myApp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
	l=['Name','Number','Marks','Address']

admin.site.register(Student,StudentAdmin)