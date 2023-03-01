from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='Home'),  # Home   
    path('mt5/', views.mt5_view, name='MT5 license'), # Check MT5 License
    path('login/<int:id>/', views.login, name='login')
]