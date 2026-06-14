from datetime import date

from django import forms

from .models import Budget


class BudgetForm(forms.ModelForm):

    MONTH_CHOICES = [
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December"),
    ]

    month = forms.ChoiceField(
        choices=MONTH_CHOICES
    )

    year = forms.ChoiceField(
        choices=[
            (year, year)
            for year in range(2025, 2036)
        ]
    )

    class Meta:
        model = Budget

        fields = (
            "category",
            "amount",
        )

    def save(self, commit=True):

        budget = super().save(commit=False)

        month = int(self.cleaned_data["month"])
        year = int(self.cleaned_data["year"])

        budget.budget_month = date(
            year,
            month,
            1
        )

        if commit:
            budget.save()

        return budget