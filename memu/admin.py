from django.contrib import admin
from .models import Memu

# Register your models here.

class memuAdmin(admin.ModelAdmin):
  list_display = ("item", "size", "temp","price")
  
admin.site.register(Memu, memuAdmin)

