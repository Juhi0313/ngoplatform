from django.contrib import admin
from .models import NGO, Event

@admin.register(NGO)
class NGOAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_person', 'email', 'city', 'state', 'created_at']
    list_filter = ['state', 'city', 'created_at']
    search_fields = ['name', 'contact_person', 'email', 'registration_number']
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'ngo', 'date_time', 'city', 'state', 'created_at']
    list_filter = ['state', 'city', 'date_time', 'created_at']
    search_fields = ['title', 'description', 'ngo__name']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'date_time'


