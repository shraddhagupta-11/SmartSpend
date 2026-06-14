from django import forms

from .models import Goal


class GoalForm(forms.ModelForm):

    target_date = forms.DateField(
        widget=forms.DateInput(
            attrs={"type": "date"}
        ),
        required=False
    )

    class Meta:
        model = Goal

        fields = (
            "title",
            "description",
            "target_amount",
            "current_amount",
            "target_date",
        )