# Generated by Django 3.2.6 on 2022-01-28 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0038_rename_class_learning_filename'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='Sentence2',
            field=models.TextField(blank=True),
        ),
    ]
