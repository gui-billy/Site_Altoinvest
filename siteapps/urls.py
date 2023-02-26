from django.urls import path

from siteapps.views import home, mt5_view

urlpatterns = [
    path('', home),  # Home   
    path('mt5/', mt5_view),
]