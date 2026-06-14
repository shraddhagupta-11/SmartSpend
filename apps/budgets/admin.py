from django.contrib import admin

from .models import Budget


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "category",
        "budget_month",
        "amount",
    )

    list_filter = (
        "budget_month",
        "category",
    )