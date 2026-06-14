from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import (
    ProfileUpdateForm,
    UserRegistrationForm,
    UserUpdateForm,
)


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(
                request,
                "Account created successfully."
            )

            return redirect("profile")
    else:
        form = UserRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form}
    )


@login_required
def profile(request):
    return render(
        request,
        "accounts/profile.html"
    )


@login_required
def profile_update(request):

    if request.method == "POST":

        user_form = UserUpdateForm(
            request.POST,
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user.profile
        )

        if (
            user_form.is_valid()
            and profile_form.is_valid()
        ):
            user_form.save()
            profile_form.save()

            messages.success(
                request,
                "Profile updated."
            )

            return redirect("profile")

    else:

        user_form = UserUpdateForm(
            instance=request.user
        )

        profile_form = ProfileUpdateForm(
            instance=request.user.profile
        )

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }

    return render(
        request,
        "accounts/profile_update.html",
        context
    )