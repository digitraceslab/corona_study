"""polar_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

import users.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='main'), name='logout'),
    path('registration/', users.views.RegistrationView.as_view(), name='registration'),
    path('consent/', users.views.ConsentView.as_view(), name='consent'),
    path('consent-success/', users.views.ConsentSuccessView.as_view(), name='consent-success'),
    path('privacy/', users.views.PrivacyView.as_view(), name='privacy'),
    path('remove/', users.views.Remove_authorization.as_view(), name='remove'),
    path('', users.views.AboutView.as_view(), name='main'),
    path('about/', users.views.AboutView.as_view(), name='about'),
    path('about_initial/', users.views.AboutView.as_view(), name='about_initial'),
    path('email_subscribers/', users.views.EmailSubscribersView.as_view(), name='email_subscribers'),
    path('token/', users.views.AddAuthTokenView.as_view(), name='auth_return'),
    path('authorize/', users.views.GetAuthenticationView.as_view(), name='auth'),
    path('faq/', users.views.FAQView.as_view(), name='faq'),
    path(r'surveys/', include('survey.urls'))
]
