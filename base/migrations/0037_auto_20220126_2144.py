# Generated by Django 3.2.6 on 2022-01-26 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_auto_20220126_1309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learning',
            old_name='FileName',
            new_name='Class',
        ),
        migrations.RenameField(
            model_name='learning',
            old_name='url',
            new_name='Research',
        ),
        migrations.RenameField(
            model_name='learning',
            old_name='via',
            new_name='Topic',
        ),
    ]