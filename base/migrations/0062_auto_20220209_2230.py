# Generated by Django 3.2.6 on 2022-02-09 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0061_auto_20220209_2225'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='analytics_apps_stock_picker',
            new_name='analytics_apps_trade_ideas',
        ),
        migrations.AlterModelOptions(
            name='analytics_apps_trade_ideas',
            options={'verbose_name': 'Analytics Apps Trade Ideas', 'verbose_name_plural': 'Analytics Apps Trade Ideas'},
        ),
    ]
