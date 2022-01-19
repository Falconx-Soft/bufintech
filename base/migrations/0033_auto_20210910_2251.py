# Generated by Django 3.2.3 on 2021-09-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0032_auto_20210910_2030'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsLetterSubscribe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'NewsLetter Subscribe',
                'verbose_name_plural': 'NewsLetter Subscribe',
            },
        ),
        migrations.AlterModelOptions(
            name='market',
            options={'verbose_name': 'Market Outlook', 'verbose_name_plural': 'Market Outlook'},
        ),
    ]
