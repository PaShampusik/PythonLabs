from django.urls import re_path
import django
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    logout_then_login,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

app_name = "account"

urlpatterns = [
    # login / logout urls
    re_path(r"^login/$", LoginView.as_view(), name="login"),
    re_path(r"^logout/$", LogoutView.as_view(), name="logout"),
    re_path(r"^logout-then-login/$", logout_then_login, name="logout_then_login"),
    re_path(
        r"^password-change/$", PasswordChangeView.as_view(), name="password_change"
    ),
    re_path(
        r"^password-change-done/$",
        PasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    re_path(r"^password-reset/$", PasswordResetView.as_view(), name="password_reset"),
    re_path(
        r"^password-reset-done/$",
        PasswordResetDoneView.as_view(),
        name="password_reset_done",
    ),
    re_path(
        r"^password_reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    re_path(
        r"^password-reset-complete/$",
        PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    re_path(r"^register/$", views.register, name="register"),
]
