# Generated by Django 3.2.6 on 2022-02-03 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0048_social_network'),
    ]

    operations = [
        migrations.RenameField(
            model_name='table',
            old_name='Clickable',
            new_name='Username',
        ),
    ]
