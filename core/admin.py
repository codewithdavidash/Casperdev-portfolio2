from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title', 'created_at']
    
admin.site.register(Project, ProjectAdmin)
admin.site.register(Blog)