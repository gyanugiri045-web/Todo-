from django.contrib import admin
from .models import Task

# Register your models here.

admin.site.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = ['title','description','due_date','priority','created_at']
    search_fields = ['title']
    list_filter = ['completed','priority']
