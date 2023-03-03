from django.contrib import admin

from .models import Stoploss, UsrAlgo


@admin.register(Stoploss)
class CStopLoss(admin.ModelAdmin):
    ...


@admin.register(UsrAlgo)
class CUsrAlgo(admin.ModelAdmin):
    ...
