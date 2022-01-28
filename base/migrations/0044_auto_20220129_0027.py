# Generated by Django 3.2.6 on 2022-01-28 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0043_learning_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='money_making_trading',
            name='Class',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='money_making_trading',
            name='Expiration_Date',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='money_making_trading',
            name='Identifier',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='money_making_trading',
            name='Initial_Inv',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='money_making_trading',
            name='ROI',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
        migrations.AddField(
            model_name='money_making_trading',
            name='ReCap',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
        migrations.AlterField(
            model_name='money_making_trading',
            name='Podcast',
            field=models.CharField(blank=True, default='none', max_length=50),
        ),
    ]
