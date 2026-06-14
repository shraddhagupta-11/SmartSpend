from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

from apps.goals.models import Goal
from apps.expenses.models import Expense
from apps.income.models import Income

from .services import get_financial_insights
import json

from .services import (
    get_budget_performance,
    get_category_spending,
    get_financial_summary,
    get_monthly_expense_trend,
)


@login_required
def dashboard(request):

    summary = get_financial_summary(
        request.user
    )

    category_spending = (
        get_category_spending(
            request.user
        )
    )

    chart_labels = []
    chart_values = []

    for item in category_spending:

        chart_labels.append(
            item["category__name"]
        )

        chart_values.append(
            float(item["total"])
        )
    


    budget_performance = (
        get_budget_performance(
            request.user
        )
    )

    expense_trend = (
        get_monthly_expense_trend(
            request.user
        )
    )

    active_goals = (
        Goal.objects.filter(
            user=request.user
        )[:5]
    )

    recent_expenses = Expense.objects.filter(
        user=request.user
    ).order_by(
        "-expense_date",
        "-id"
    )[:5]

    recent_income = Income.objects.filter(
        user=request.user
    ).order_by(
        "-income_date",
        "-id"
    )[:5]

    recent_activity = []

    for expense in recent_expenses:

        recent_activity.append(
            {
                "type": "expense",
                "title": expense.title,
                "amount": expense.amount,
                "date": expense.expense_date,
            }
        )

    for income in recent_income:

        recent_activity.append(
            {
                "type": "income",
                "title": income.title,
                "amount": income.amount,
                "date": income.income_date,
            }
        )

    recent_activity = sorted(
        recent_activity,
        key=lambda x: x["date"],
        reverse=True
    )[:5]

    insights = get_financial_insights(
        request.user,
        budget_performance,
        active_goals,
        summary["savings_rate"]
    )

    context = {
        **summary,

        "category_spending": category_spending,

        "budget_performance": budget_performance,

        "active_goals": active_goals,

        "recent_activity": recent_activity,

        "insights": insights,

        "chart_labels":
            json.dumps(chart_labels),

        "chart_values":
            json.dumps(chart_values),

        "income_expense_labels":
            json.dumps([
                "Income",
                "Expenses"
            ]),

        "income_expense_values":
            json.dumps([
                float(summary["total_income"]),
                float(summary["total_expenses"])
            ]),

        "expense_trend_labels":
            json.dumps(
                expense_trend["labels"]
            ),

        "expense_trend_values":
            json.dumps(
                expense_trend["values"]
            ),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )

def home(request):

    if request.user.is_authenticated:

        return redirect(
            "dashboard"
        )

    return render(
        request,
        "core/home.html"
    )