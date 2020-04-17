from django.contrib import admin

# Register your models here.
from .models import Course #from module, import your class

admin.site.register(Course) # register your class with admin section
