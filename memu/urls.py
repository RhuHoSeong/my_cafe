from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('memu/', views.memu, name='memu'),
    path('memu/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
    
]