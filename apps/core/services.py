from django.db.models import Sum
from django.db.models.functions import TruncMonth

from apps.budgets.models import Budget
from apps.expenses.models import Expense
from apps.income.models import Income


def get_financial_summary(user):

    total_income = (
        Income.objects.filter(
            user=user
        ).aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )

    total_expenses = (
        Expense.objects.filter(
            user=user
        ).aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )

    net_balance = (
        total_income -
        total_expenses
    )

    savings_rate = 0

    if total_income > 0:

        savings_rate = round(
            (
                net_balance /
                total_income
            ) * 100,
            2
        )

    return {
        "total_income": total_income,
        "total_expenses": total_expenses,
        "net_balance": net_balance,
        "savings_rate": savings_rate,
    }


def get_category_spending(user):

    return (
        Expense.objects.filter(
            user=user
        )
        .values("category__name")
        .annotate(
            total=Sum("amount")
        )
        .order_by("-total")
    )


def get_budget_performance(user):

    budgets = Budget.objects.filter(
        user=user
    )

    results = []

    for budget in budgets:

        spent = Expense.objects.filter(
            user=user,
            category=budget.category
        ).aggregate(
            total=Sum("amount")
        )["total"] or 0

        usage_percentage = 0

        if budget.amount > 0:

            usage_percentage = round(
                (
                    spent /
                    budget.amount
                ) * 100,
                2
            )

        results.append(
            {
                "category":
                    budget.category.name,

                "budget_amount":
                    budget.amount,

                "spent":
                    spent,

                "usage_percentage":
                    usage_percentage,
            }
        )

    return results


def get_financial_insights(
    user,
    budgets,
    goals,
    savings_rate
):

    insights = []

    for budget in budgets:

        if budget["usage_percentage"] >= 90:

            insights.append(
                f"⚠ {budget['category']} budget is "
                f"{budget['usage_percentage']}% utilized."
            )

        elif budget["usage_percentage"] >= 75:

            insights.append(
                f"ℹ {budget['category']} budget is "
                f"{budget['usage_percentage']}% utilized."
            )

    for goal in goals:

        if goal.progress_percentage >= 90:

            insights.append(
                f"🎯 {goal.title} goal is nearly complete."
            )

        elif goal.progress_percentage >= 75:

            insights.append(
                f"🎯 {goal.title} goal is "
                f"{goal.progress_percentage}% complete."
            )

    if savings_rate < 0:

        insights.append(
            "⚠ Your expenses exceed your income."
        )

    elif savings_rate >= 30:

        insights.append(
            f"📈 Excellent savings rate "
            f"of {savings_rate}%."
        )

    return insights

def get_monthly_expense_trend(user):

    monthly_data = (
        Expense.objects
        .filter(user=user)
        .annotate(
            month=TruncMonth("expense_date")
        )
        .values("month")
        .annotate(
            total=Sum("amount")
        )
        .order_by("month")
    )

    labels = []
    values = []

    for item in monthly_data:

        labels.append(
            item["month"].strftime("%b %Y")
        )

        values.append(
            float(item["total"])
        )

    return {
        "labels": labels,
        "values": values,
    }