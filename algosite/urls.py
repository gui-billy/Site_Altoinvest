from django.urls import path

from siteapps.views import home, run_app

urlpatterns = [
    path('',home),
    path('mt5/', run_app),
]
