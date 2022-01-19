# Generated by Django 3.2.3 on 2021-09-08 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_auto_20210909_0330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equity_private',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
        migrations.AlterField(
            model_name='equity_public',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
        migrations.AlterField(
            model_name='learning',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
        migrations.AlterField(
            model_name='market',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
        migrations.AlterField(
            model_name='money_making_investing',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
        migrations.AlterField(
            model_name='money_making_trading',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
        migrations.AlterField(
            model_name='table',
            name='url',
            field=models.FileField(upload_to='PDF'),
        ),
    ]
