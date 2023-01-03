from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='gradi-acasa'),
    path('about/', views.about, name='gradi-about'),
    path('inscriere2/', views.formular, name='gradi-inscriere'),
    path('test/', views.test, name='gradi-test'),
    path('inscriere/', views.insc, name='gradi-inscriere2'),
    path('login/', views.log, name='gradi-login'),
    path('register/', views.reg, name='gradi-register'),
     path('logout/', views.logoutuser, name='logout'),
]
