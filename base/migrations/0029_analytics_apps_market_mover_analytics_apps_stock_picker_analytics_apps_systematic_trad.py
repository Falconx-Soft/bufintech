# Generated by Django 3.2.3 on 2021-09-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0028_rename_file_name_learning_filename'),
    ]

    operations = [
        migrations.CreateModel(
            name='analytics_apps_market_mover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='analytics_apps_stock_picker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='analytics_apps_systematic_trad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
