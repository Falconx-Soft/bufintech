# Generated by Django 3.2.3 on 2021-09-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_merge_0012_auto_20210908_2054_0012_auto_20210908_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='Sentence',
            field=models.TextField(default='null'),
        ),
    ]
