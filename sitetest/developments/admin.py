from django.contrib import admin
from .models import LabTheme

@admin.register(LabTheme)
class LabThemAdmin(admin.ModelAdmin):
    list_display = ['name']

