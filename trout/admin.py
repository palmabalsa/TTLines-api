from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import FishingLogEntry

# Register your models here.

admin.site.register(FishingLogEntry)
