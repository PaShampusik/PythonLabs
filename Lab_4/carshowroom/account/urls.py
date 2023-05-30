from django.urls import re_path
import django
from . import views
from django.contrib.auth.views import LoginView, LogoutView, logout_then_login, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [

    # login / logout urls
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^logout/$', LogoutView.as_view(), name='logout'),
    re_path(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    re_path(r'^$', views.dashboard, name='dashboard'),
    re_path(r'^password-change/$', PasswordChangeView, name='password_change'),
    re_path(r'^password-change/done/$', PasswordChangeDoneView, name='password_change_done'),
    re_path(r'^password-reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
    re_path(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', name='password_reset_done'),
    re_path(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', name='password_reset_confirm'),
    re_path(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', name='password_reset_complete'),
]