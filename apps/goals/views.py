from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import GoalForm
from .models import Goal


@login_required
def goal_list(request):

    goals = Goal.objects.filter(
        user=request.user
    )

    return render(
        request,
        "goals/goal_list.html",
        {"goals": goals}
    )


@login_required
def goal_create(request):

    if request.method == "POST":

        form = GoalForm(request.POST)

        if form.is_valid():

            goal = form.save(commit=False)

            goal.user = request.user

            goal.save()

            messages.success(
                request,
                "Goal created successfully."
            )

            return redirect("goal_list")

    else:

        form = GoalForm()

    return render(
        request,
        "goals/goal_form.html",
        {"form": form}
    )


@login_required
def goal_update(request, pk):

    goal = get_object_or_404(
        Goal,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        form = GoalForm(
            request.POST,
            instance=goal
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Goal updated successfully."
            )

            return redirect(
                "goal_list"
            )

    else:

        form = GoalForm(
            instance=goal
        )

    return render(
        request,
        "goals/goal_form.html",
        {"form": form}
    )


@login_required
def goal_delete(request, pk):

    goal = get_object_or_404(
        Goal,
        pk=pk,
        user=request.user
    )

    if request.method == "POST":

        goal.delete()

        messages.success(
            request,
            "Goal deleted successfully."
        )

        return redirect(
            "goal_list"
        )

    return render(
        request,
        "goals/goal_delete.html",
        {"goal": goal}
    )