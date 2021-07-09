"""veterinaria URL Configuration

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
from veterinaria.settings import TEMPLATES
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('servicios', TemplateView.as_view(template_name='servicios.html'), name='servicios'),
    path('quienes_somos', TemplateView.as_view(template_name='quienes_somos.html'), name='quienes_somos'),
    path('contactanos', TemplateView.as_view(template_name='contactanos.html'), name='contactanos'),
    # path('login', TemplateView.as_view(template_name='login.html'), name='login'),
    path('', include('apps.Registro.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='Usuario/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='Usuario/logout.html'), name='logout'),
    path('base', TemplateView.as_view(template_name='Registro/base.html'), name='base'),
    path('registrar', TemplateView.as_view(template_name='Usuario/registrar.html'), name='registrar'),
]
