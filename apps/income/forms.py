from django import forms
from datetime import date

from .models import Income


class IncomeForm(forms.ModelForm):

    income_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "value": date.today().isoformat()
            }
        )
    )

    class Meta:
        model = Income

        fields = (
            "title",
            "source",
            "amount",
            "description",
            "income_date",
        )