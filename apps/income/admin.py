from django.contrib import admin

from .models import Income


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "amount",
        "source",
        "user",
        "income_date",
    )

    list_filter = (
        "source",
        "income_date",
    )

    search_fields = (
        "title",
        "description",
    )