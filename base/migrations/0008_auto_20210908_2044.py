# Generated by Django 3.1.6 on 2021-09-08 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_equity_private_ticker'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='Date',
            field=models.DateField(default='2020-12-29'),
        ),
        migrations.AlterField(
            model_name='equity_private',
            name='Date',
            field=models.DateField(),
        ),
    ]
