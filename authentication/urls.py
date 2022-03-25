"""authentication URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView, RedirectView
from dj_rest_auth.registration.views import VerifyEmailView
from django.contrib.auth import views as auth_views
from dj_rest_auth.views import PasswordResetConfirmView,PasswordResetView,PasswordChangeView,UserDetailsView




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('dj-rest-auth/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('dj-rest-auth/password-reset/',PasswordResetView.as_view(),name="password_reset"),
    path('dj-rest-auth/password-change/',PasswordChangeView.as_view(),name="password_change"),
    path('dj-rest-auth/password/reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('dj-rest-auth/user-details/',UserDetailsView.as_view(),name="user_details_view"),
    path('users/', include('allauth.urls')),
]
