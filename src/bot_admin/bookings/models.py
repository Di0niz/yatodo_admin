from django.db import models
from django.utils.translation import gettext_lazy as _

from bot_admin.events.models import Event


class Slot(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="slots", verbose_name=_("Event"))
    time_slot = models.DateTimeField(verbose_name=_("Time Slot"))

    def __str__(self):
        return f"Slot for {self.event.name} at {self.time_slot}"

    class Meta:
        verbose_name = _("Slot")
        verbose_name_plural = _("Slots")
        ordering = ["time_slot"]


class BookingSlot(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="bookings", verbose_name=_("Slot"))
    telegram_id = models.CharField(max_length=255, verbose_name=_("Telegram ID"), null=True, blank=True)
    canceled_dt = models.DateTimeField(verbose_name=_("Canceled Date"), null=True, blank=True)

    def __str__(self):
        status = "Canceled" if self.canceled_dt else "Active"
        return f"Booking for {self.slot} ({status})"

    class Meta:
        verbose_name = _("Booking Slot")
        verbose_name_plural = _("Booking Slots")
        ordering = ["slot__time_slot"]
