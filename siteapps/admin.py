from django.contrib import admin

from .models import Stoploss


@admin.register(Stoploss)
class c_stoploss(admin.ModelAdmin): ...
