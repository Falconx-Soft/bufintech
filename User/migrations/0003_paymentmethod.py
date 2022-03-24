# Generated by Django 3.2.6 on 2022-03-22 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_accountscheck'),
    ]

    operations = [
        migrations.CreateModel(
            name='paymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(max_length=100)),
                ('method', models.CharField(max_length=10000)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
    ]