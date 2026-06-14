from django import forms
from datetime import date
from .models import Expense


class ExpenseForm(forms.ModelForm):

    expense_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "value": date.today().isoformat()
            }
        )
    )
    
    class Meta:
        model = Expense

        fields = (
            "title",
            "category",
            "amount",
            "description",
            "expense_date",
        )