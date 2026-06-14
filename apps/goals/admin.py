from django.contrib import admin

from .models import Goal


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "user",
        "target_amount",
        "current_amount",
        "target_date",
    )

    search_fields = (
        "title",
    )