from django.contrib import admin
from .models import ClassName, Student, Attendance


# Register your models here.
myModels  = [ClassName, Student, Attendance]
admin.site.register(myModels)