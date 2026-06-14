from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    
    path(
    "",
    RedirectView.as_view(
        pattern_name="login",
        permanent=False
        ),
    ),

    path(
        "register/",
        views.register,
        name="register",
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path(
        "profile/",
        views.profile,
        name="profile",
    ),

    path(
        "profile/update/",
        views.profile_update,
        name="profile_update",
    ),
]