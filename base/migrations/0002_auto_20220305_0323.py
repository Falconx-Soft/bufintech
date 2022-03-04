# Generated by Django 3.2.6 on 2022-03-04 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity',
            name='Description',
            field=models.CharField(blank=True, default='none', max_length=5100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='Language',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='Market',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=1100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='Podcast',
            field=models.CharField(blank=True, max_length=1100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='Product',
            field=models.CharField(blank=True, default='none', max_length=1100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='Ticker',
            field=models.CharField(blank=True, max_length=1100),
        ),
        migrations.AlterField(
            model_name='equity',
            name='Youtube',
            field=models.CharField(blank=True, max_length=1100),
        ),
    ]
