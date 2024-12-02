from django.contrib import admin

from bot_admin.bookings.models import Slot, BookingSlot


@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ("event", "time_slot")
    list_filter = ("event__type",)
    search_fields = ("event__name",)
    ordering = ("time_slot",)


@admin.register(BookingSlot)
class BookingSlotAdmin(admin.ModelAdmin):
    list_display = ("slot", "telegram_id", "canceled_dt")
    list_filter = ("slot__event__type", "canceled_dt")
    search_fields = ("slot__event__name", "telegram_id")
    ordering = ("slot__time_slot",)
