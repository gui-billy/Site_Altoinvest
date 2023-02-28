from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),  # Home   
    path('mt5/', views.mt5_view),
]