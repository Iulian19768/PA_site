"""pa_proiect URL Configuration

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gradi.urls')),
    path('about/', include('gradi.urls')),
    path('inscriere2/', include('gradi.urls')),
    path('test/', include('gradi.urls')),
    path('inscriere/', include('gradi.urls')),
    path('login/', include('gradi.urls')),
    path('register/', include('gradi.urls')),
]
