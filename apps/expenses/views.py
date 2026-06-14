from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.db.models import Sum

from .forms import ExpenseForm
from .models import Expense


@login_required
def expense_list(request):

    expenses = (
        Expense.objects
        .filter(user=request.user)
        .select_related("category")
    )

    total_expenses = (
        expenses.aggregate(
            total=Sum("amount")
        )["total"]
        or 0
    )

    context = {

        "expenses": expenses,

        "total_expenses":
            total_expenses,

    }

    return render(
        request,
        "expenses/expense_list.html",
        context
    )


@login_required
def expense_create(request):

    if request.method == "POST":

        form = ExpenseForm(request.POST)

        if form.is_valid():

            expense = form.save(commit=False)

            expense.user = request.user

            expense.save()

            messages.success(
                request,
                "Expense created successfully."
            )

            return redirect("expense_list")

    else:

        form = ExpenseForm()

    return render(
        request,
        "expenses/expense_form.html",
        {"form": form}
    )


@login_required
def expense_update(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = ExpenseForm(
            request.POST,
            instance=expense
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Expense updated successfully."
            )

            return redirect("expense_list")

    else:

        form = ExpenseForm(
            instance=expense
        )

    return render(
        request,
        "expenses/expense_form.html",
        {"form": form}
    )


@login_required
def expense_delete(request, pk):

    expense = get_object_or_404(
        Expense,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        expense.delete()

        messages.success(
            request,
            "Expense deleted successfully."
        )

        return redirect(
            "expense_list"
        )

    return render(
        request,
        "expenses/expense_delete.html",
        {"expense": expense}
    )