# Generated by Django 3.2.6 on 2022-02-04 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0057_auto_20220205_0227'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='money_making_investing',
            name='Date',
        ),
        migrations.RemoveField(
            model_name='money_making_investing',
            name='Date_Company',
        ),
        migrations.RemoveField(
            model_name='money_making_investing',
            name='Short_Name',
        ),
    ]