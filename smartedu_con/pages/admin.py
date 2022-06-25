from atexit import register
from django.contrib import admin
from .models import Contact

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name','date')
    list_display_links = ('first_name', 'last_name','date')