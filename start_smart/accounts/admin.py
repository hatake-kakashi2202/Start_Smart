from django.contrib import admin
from django.contrib.auth.models import User
from .models import Startup, Mentor

# Register your models here.
admin.site.register(Startup)
admin.site.register(Mentor)