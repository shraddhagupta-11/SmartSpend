from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import IncomeForm
from .models import Income
from django.db.models import Sum


@login_required
def income_list(request):

    incomes = (
        Income.objects
        .filter(user=request.user)
    )

    total_income = (
        incomes.aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )

    context = {

        "incomes": incomes,

        "total_income":
            total_income,

    }

    return render(
        request,
        "income/income_list.html",
        context
    )


@login_required
def income_create(request):

    if request.method == "POST":

        form = IncomeForm(request.POST)

        if form.is_valid():

            income = form.save(commit=False)

            income.user = request.user

            income.save()

            messages.success(
                request,
                "Income created successfully."
            )

            return redirect("income_list")

    else:

        form = IncomeForm()

    return render(
        request,
        "income/income_form.html",
        {"form": form}
    )


@login_required
def income_update(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = IncomeForm(
            request.POST,
            instance=income
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Income updated successfully."
            )

            return redirect("income_list")

    else:

        form = IncomeForm(
            instance=income
        )

    return render(
        request,
        "income/income_form.html",
        {"form": form}
    )


@login_required
def income_delete(request, pk):

    income = get_object_or_404(
        Income,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        income.delete()

        messages.success(
            request,
            "Income deleted successfully."
        )

        return redirect(
            "income_list"
        )

    return render(
        request,
        "income/income_delete.html",
        {"income": income}
    )