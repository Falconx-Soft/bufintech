# Generated by Django 3.2.6 on 2022-03-03 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20220303_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='money_making_investing',
            name='ROI',
            field=models.IntegerField(blank=True, default='none', max_length=50),
        ),
    ]
