from django.contrib import admin
from .models import Info

# Register your models here.

@admin.register(Info)
class StatistAdmin(admin.ModelAdmin):
    list_display = ['date', 'views', 'clicks', 'cost']
    list_display_links = ['date', 'views']