from django.contrib import admin
from .models import Profile


# Register your models here.
myModels  = [Profile]
admin.site.register(myModels)