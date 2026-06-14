from django.conf import settings
from django.db import models


class Goal(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="goals"
    )

    title = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    target_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    current_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    target_date = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["target_date"]

    @property
    def progress_percentage(self):

        if self.target_amount == 0:
            return 0

        return round(
            (self.current_amount / self.target_amount) * 100,
            2
        )

    @property
    def remaining_amount(self):

        return (
            self.target_amount -
            self.current_amount
        )

    def __str__(self):
        return self.title