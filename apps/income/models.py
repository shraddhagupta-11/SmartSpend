from django.conf import settings
from django.db import models


class Income(models.Model):

    INCOME_SOURCES = [
        ("salary", "Salary"),
        ("freelance", "Freelance"),
        ("business", "Business"),
        ("investment", "Investment"),
        ("gift", "Gift"),
        ("other", "Other"),
    ]

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="incomes"
    )

    title = models.CharField(
        max_length=255
    )

    source = models.CharField(
        max_length=50,
        choices=INCOME_SOURCES
    )

    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField(
        blank=True
    )

    income_date = models.DateField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["-income_date"]

    def __str__(self):
        return f"{self.title} - ₹{self.amount}"