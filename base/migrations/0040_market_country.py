# Generated by Django 3.2.6 on 2022-01-28 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0039_aboutus_sentence2'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='Country',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
