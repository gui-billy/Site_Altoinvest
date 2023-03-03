from django.contrib.auth.models import User  # noqa: F401
from django.db import models


class Stoploss(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class UsrAlgo(models.Model):
    name = models.CharField(max_length=65, verbose_name=('name'))
    description = models.CharField(max_length=165)
    platform = models.CharField(max_length=65)
    account_type = models.CharField(max_length=65)
    market_type = models.CharField(max_length=65)
    system_type = models.CharField(max_length=65)
    volume = models.CharField(max_length=65)
    stoploss = models.CharField(max_length=65)
    takeprofit = models.CharField(max_length=65)
    tradetime = models.CharField(max_length=65)
    closetime = models.CharField(max_length=65)
    indicators = models.CharField(max_length=120)
    timeframe = models.CharField(max_length=65)
    magic = models.CharField(max_length=65)
    order = models.CharField(max_length=65)
    breakeven = models.CharField(max_length=65)
    trailing = models.CharField(max_length=65)
    money_goal = models.CharField(max_length=65)
    setup = models.TextField()
    images = models.ImageField(
        upload_to='siteapps/images/%Y/%m/%d/', blank=True, default='')

    def __str__(self):
        return self.name
