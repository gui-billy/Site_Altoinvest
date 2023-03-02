# Generated by Django 4.1.7 on 2023-03-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteapps', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='usr_algo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('description', models.CharField(max_length=165)),
                ('platform', models.CharField(max_length=65)),
                ('account_type', models.CharField(max_length=65)),
                ('market_type', models.CharField(max_length=65)),
                ('system_type', models.CharField(max_length=65)),
                ('volume', models.CharField(max_length=65)),
                ('stoploss', models.CharField(max_length=65)),
                ('takeprofit', models.CharField(max_length=65)),
                ('tradetime', models.CharField(max_length=65)),
                ('closetime', models.CharField(max_length=65)),
                ('indicators', models.CharField(max_length=120)),
                ('timeframe', models.CharField(max_length=65)),
                ('magic', models.CharField(max_length=65)),
                ('order', models.CharField(max_length=65)),
                ('breakeven', models.CharField(max_length=65)),
                ('trailing', models.CharField(max_length=65)),
                ('money_goal', models.CharField(max_length=65)),
                ('setup', models.TextField()),
                ('images', models.ImageField(blank=True, default='', upload_to='siteapps/images/%Y/%m/%d/')),
            ],
        ),
    ]
