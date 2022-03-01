from django.contrib import admin
from .models import Checklist, ChecklistItem

@admin.register(Checklist)
class ChecklistAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_deleted', 'is_archived', 'created_on', 'updated_on']

@admin.register(ChecklistItem)
class ChecklistItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'is_checked', 'created_on', 'updated_on', 'checklist']