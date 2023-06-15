"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.urls import path
from mainapp.views import IndexView, UsersView, CreateUsersView, ContactView, LoginView, IndexInternoView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('usuarios', UsersView.as_view(), name='users'),
    path('nuevousuario', CreateUsersView.as_view(), name='newuser'),    
    path('contacto', ContactView.as_view(), name='contact'),
    path('entrar', LoginView.as_view(), name="login"),
    path('salir', LogoutView.as_view(), name='logout'),
    path('internalindex', login_required(IndexInternoView.as_view()), name='internalindex'),

]
