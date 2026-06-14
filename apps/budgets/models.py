from django.conf import settings
from django.db import models
from django.db.models import Sum

from apps.expenses.models import Category


class Budget(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="budgets"
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    budget_month = models.DateField(
        help_text="Select any date within the budget month"
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-budget_month"]

        unique_together = (
            "user",
            "category",
            "budget_month",
        )
        

    def __str__(self):
        return (
            f"{self.category} Budget "
            f"({self.budget_month.strftime('%B %Y')})"
        )
    
    @property
    def spent_amount(self):

        from apps.expenses.models import Expense

        total = Expense.objects.filter(
            user=self.user,
            category=self.category,
            expense_date__month=self.budget_month.month,
            expense_date__year=self.budget_month.year,
        ).aggregate(
            total=Sum("amount")
        )["total"]

        return total or 0


    @property
    def remaining_amount(self):

        return self.amount - self.spent_amount


    @property
    def usage_percentage(self):

        if self.amount == 0:
            return 0

        return round(
            (self.spent_amount / self.amount) * 100,
            2
        )