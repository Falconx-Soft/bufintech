# Generated by Django 3.2.6 on 2022-01-28 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0040_market_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='learning',
            name='Class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]