from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import json

from apps.goals.models import Goal

from apps.core.services import (
    get_budget_performance,
    get_category_spending,
    get_financial_summary,
    get_monthly_expense_trend,
    get_financial_insights,
)


@login_required
def analytics_dashboard(request):

    summary = get_financial_summary(
        request.user
    )

    category_spending = (
        get_category_spending(
            request.user
        )
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

    goals = Goal.objects.filter(
        user=request.user
    )

    insights = get_financial_insights(
        request.user,
        budget_performance,
        goals,
        summary["savings_rate"]
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

    context = {

        **summary,

        "budget_performance":
            budget_performance,

        "goals":
            goals,

        "insights":
            insights,

        "chart_labels":
            json.dumps(chart_labels),

        "chart_values":
            json.dumps(chart_values),

        "expense_trend_labels":
            json.dumps(
                expense_trend["labels"]
            ),

        "expense_trend_values":
            json.dumps(
                expense_trend["values"]
            ),

        "category_spending": category_spending,
    }

    return render(
        request,
        "analytics/analytics.html",
        context
    )