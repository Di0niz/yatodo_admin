from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

class EventType(models.TextChoices):
    WEBINAR = "webinar", _("Webinar")
    MENTOR_SESSION = "mentor_session", _("Mentor Session")


class Event(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    date = models.DateTimeField(verbose_name=_("Date"))
    description = models.TextField(verbose_name=_("Description"), blank=True)
    type = models.CharField(
        max_length=20,
        choices=EventType.choices,
        default=EventType.WEBINAR,
        verbose_name=_("Event Type")
    )

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")
        ordering = ["date"]

class SubscribeUser(models.Model):
    title = models.CharField(max_length=100, verbose_name="Nikname")
    telegram_id = models.CharField(max_length=50, unique=True, verbose_name="Telegram ID")
    date_registered = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="participants", verbose_name="Мероприятие")

    class Meta:
        verbose_name = "Подписчик"
        verbose_name_plural = "Подписчики"
        ordering = ['-date_registered']

    def __str__(self):
        return f"{self.first_name} {self.last_name} (Telegram ID: {self.telegram_id})"
