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
from dj_rest_auth.views import PasswordResetConfirmView,PasswordResetView,PasswordChangeView,UserDetailsView,LoginView,LogoutView,UserDetailsSerializer




urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1', include('dj_rest_auth.urls')),
    path('api/v1/registration/', include('dj_rest_auth.registration.urls')),
    path('api/v1/account-confirm-email/', VerifyEmailView.as_view(), name='account_email_verification_sent'),
    path('api/v1/Login/', LoginView.as_view(), name='Login'),
    path('api/v1/Logout/', LogoutView.as_view(), name='Logout'),
    path('api/v1/password-reset/',PasswordResetView.as_view(),name="password_reset"),
    path('api/v1/password-change/',PasswordChangeView.as_view(),name="password_change"),
    path('api/v1/password/reset/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('api/v1/user-details/',UserDetailsView.as_view(),name="user_details_view"),
    path('users/', include('allauth.urls')),
]
