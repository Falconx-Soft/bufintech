# Generated by Django 3.2.6 on 2022-02-09 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0062_auto_20220209_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='analytics_apps_Algo_trader',
            new_name='analytical_apps_Algo_trader',
        ),
        migrations.RenameModel(
            old_name='analytics_apps_trade_ideas',
            new_name='analytical_apps_market_mover',
        ),
        migrations.RenameModel(
            old_name='analytics_apps_market_mover',
            new_name='analytical_apps_prospecting',
        ),
        migrations.RenameModel(
            old_name='analytics_apps_company_prospecting',
            new_name='analytical_apps_trade_ideas',
        ),
        migrations.AlterModelOptions(
            name='analytical_apps_algo_trader',
            options={'verbose_name': 'Analytical Apps Algo Trader', 'verbose_name_plural': 'Analytical Apps Algo Trader'},
        ),
        migrations.AlterModelOptions(
            name='analytical_apps_market_mover',
            options={'verbose_name': 'Analytical Apps Market Mover', 'verbose_name_plural': 'Analytical Apps Market Mover'},
        ),
        migrations.AlterModelOptions(
            name='analytical_apps_prospecting',
            options={'verbose_name': 'Analytical Apps Prospecting', 'verbose_name_plural': 'Analytical Apps Prospecting'},
        ),
        migrations.AlterModelOptions(
            name='analytical_apps_trade_ideas',
            options={'verbose_name': 'Analytical Apps Trade Ideas', 'verbose_name_plural': 'Analytical Apps Trade Ideas'},
        ),
    ]
