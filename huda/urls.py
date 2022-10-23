"""huda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ast import Import
from re import template
from django.contrib import admin
from django.urls import include, path
from home import views
from django.contrib.auth import views as auth_v
from django.contrib.auth.models import User

from home.forms import loginForm
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy


urlpatterns = [
    path("admin/", admin.site.urls, name='admin'),
    path('home/', views.home_page, name='home'),
    path('takePart/', views.takePart, name='takePart'),
    path('contact/', views.contactUs, name='contactUs'),
    path('signin/', auth_v.LoginView.as_view(template_name='signIn.html', redirect_authenticated_user=True,
         authentication_form=loginForm), name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.UserUpdateView.as_view(template_name='profile.html',
         success_url=reverse_lazy('profile')), name='profile'),
    path('shows/', views.shows, name='shows'),
    path('confirm/', views.confirm, name='confirm'),
    path('logout/', auth_v.LogoutView.as_view(), name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
