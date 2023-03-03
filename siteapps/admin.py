from django.contrib import admin

from .models import Clients, Stoploss, UsrAlgo


@admin.register(Stoploss)
class CStopLoss(admin.ModelAdmin):
    ...


@admin.register(UsrAlgo)
class CUsrAlgo(admin.ModelAdmin):
    ...


@admin.register(Clients)
class CClient(admin.ModelAdmin):
    ...
