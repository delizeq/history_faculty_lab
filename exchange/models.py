from django.db import models
from django.utils import timezone


class ExchangeProgram(models.Model):
    university = models.CharField("університет", max_length=255)
    country = models.CharField("країна", max_length=100)
    languages = models.CharField("мови навчання", max_length=255)
    seats = models.PositiveSmallIntegerField("кількість місць")
    deadline = models.DateField("дедлайн подачі")
    description = models.TextField("опис")

    class Meta:
        verbose_name = "програма обміну"
        verbose_name_plural = "програми обміну"
        ordering = ["deadline"]

    def __str__(self):
        return f"{self.university} ({self.country})"

    @property
    def is_open(self):
        """Прийом триває, поки не минув дедлайн (у день дедлайну ще можна подати)."""
        return self.deadline >= timezone.localdate()
