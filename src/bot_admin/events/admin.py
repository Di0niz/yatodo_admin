from django.contrib import admin
from .models import SubscribeUser, Event

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'description')
    search_fields = ('name',)

@admin.register(SubscribeUser)
class SubscribeUserAdmin(admin.ModelAdmin):
    list_display = ('title', 'telegram_id', 'event', 'date_registered')
    search_fields = ('title', 'telegram_id', 'event__name')
