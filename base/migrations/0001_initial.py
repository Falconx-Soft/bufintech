# Generated by Django 3.2.6 on 2022-03-08 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('Sentence2', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'About Us',
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='analytical_apps_Algo_trader',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Analytical Apps Algo Trader',
                'verbose_name_plural': 'Analytical Apps Algo Trader',
            },
        ),
        migrations.CreateModel(
            name='analytical_apps_market_mover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Analytical Apps Market Mover',
                'verbose_name_plural': 'Analytical Apps Market Mover',
            },
        ),
        migrations.CreateModel(
            name='analytical_apps_prospecting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Analytical Apps Prospecting',
                'verbose_name_plural': 'Analytical Apps Prospecting',
            },
        ),
        migrations.CreateModel(
            name='analytical_apps_trade_ideas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Analytical Apps Trade Ideas',
                'verbose_name_plural': 'Analytical Apps Trade Ideas',
            },
        ),
        migrations.CreateModel(
            name='equity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=100)),
                ('Product', models.CharField(blank=True, default='none', max_length=1100)),
                ('Market', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=1100)),
                ('Date', models.DateField()),
                ('Ticker', models.CharField(blank=True, max_length=1100)),
                ('Description', models.CharField(blank=True, default='none', max_length=5100)),
                ('Research', models.URLField()),
                ('Youtube', models.CharField(blank=True, max_length=1100)),
                ('Podcast', models.CharField(blank=True, max_length=1100)),
            ],
            options={
                'verbose_name': 'Equity Research',
                'verbose_name_plural': 'Equity Research',
            },
        ),
        migrations.CreateModel(
            name='learning',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(max_length=50)),
                ('Product', models.CharField(blank=True, default='N/A', max_length=50)),
                ('Topic', models.CharField(blank=True, max_length=50)),
                ('Class', models.CharField(blank=True, default='N/A', max_length=50)),
                ('Date', models.DateField(blank=True)),
                ('Description', models.CharField(blank=True, default='none', max_length=50)),
                ('Research', models.URLField()),
                ('Youtube', models.CharField(blank=True, max_length=50)),
                ('Podcast', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Learning Center',
                'verbose_name_plural': 'Learning Center',
            },
        ),
        migrations.CreateModel(
            name='ListPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Menu_Name', models.CharField(blank=True, max_length=100)),
                ('Child_Name', models.CharField(blank=True, max_length=100)),
                ('Main_Child', models.CharField(blank=True, max_length=100)),
                ('url', models.CharField(max_length=100)),
                ('Language', models.CharField(max_length=50)),
                ('Priority', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Page List',
                'verbose_name_plural': 'Page List',
            },
        ),
        migrations.CreateModel(
            name='market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product', models.CharField(blank=True, max_length=500)),
                ('Country', models.CharField(blank=True, max_length=500, null=True)),
                ('Date', models.DateField()),
                ('Description', models.CharField(blank=True, max_length=500)),
                ('Research', models.URLField()),
                ('YouTube', models.CharField(blank=True, max_length=500)),
                ('Podcast', models.CharField(blank=True, max_length=500)),
                ('Language', models.CharField(max_length=500)),
            ],
            options={
                'verbose_name': 'Market Outlook',
                'verbose_name_plural': 'Market Outlook',
            },
        ),
        migrations.CreateModel(
            name='money_making_investing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(default='en', max_length=50)),
                ('Product', models.CharField(blank=True, default='none', max_length=50)),
                ('Market', models.CharField(blank=True, default='none', max_length=50)),
                ('Entry_Date', models.DateField(blank=True)),
                ('Ticker', models.CharField(blank=True, default='none', max_length=50)),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Exit_Date', models.DateField(blank=True, null=True)),
                ('Position', models.IntegerField(blank=True)),
                ('Outcome', models.IntegerField(blank=True)),
                ('Initial_Inv', models.IntegerField(blank=True)),
                ('ROI', models.FloatField(blank=True)),
                ('ReCap', models.URLField()),
                ('Youtube', models.CharField(blank=True, max_length=50)),
                ('Podcast', models.CharField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'Money Making Investing',
                'verbose_name_plural': 'Money Making Investing',
            },
        ),
        migrations.CreateModel(
            name='money_making_trading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Language', models.CharField(default='en', max_length=50)),
                ('Product', models.CharField(blank=True, default='none', max_length=50)),
                ('Class', models.CharField(blank=True, default='none', max_length=50)),
                ('Trade_Date', models.DateField(blank=True)),
                ('Identifier', models.CharField(blank=True, default='none', max_length=50)),
                ('Outcome', models.IntegerField(blank=True, max_length=50)),
                ('Initial_Inv', models.IntegerField(blank=True, max_length=50)),
                ('ROI', models.CharField(blank=True, default='none', max_length=50)),
                ('ReCap', models.URLField()),
                ('Youtube', models.CharField(blank=True, max_length=50)),
                ('Podcast', models.CharField(blank=True, default='none', max_length=50)),
            ],
            options={
                'verbose_name': 'Money Making Trading',
                'verbose_name_plural': 'Money Making Trading',
            },
        ),
        migrations.CreateModel(
            name='NewsLetter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'NewsLetter',
                'verbose_name_plural': 'NewsLetter',
            },
        ),
        migrations.CreateModel(
            name='NewsLetterSubscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(default='', max_length=255, unique=True)),
                ('phone', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'NewsLetter Subscribers',
                'verbose_name_plural': 'NewsLetter Subscribers',
            },
        ),
        migrations.CreateModel(
            name='social_network',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sentence', models.TextField(blank=True)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Social Network',
                'verbose_name_plural': 'Social Network',
            },
        ),
        migrations.CreateModel(
            name='SocialMedia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=255)),
                ('image', models.URLField()),
                ('name', models.CharField(max_length=100)),
                ('height', models.IntegerField(default=70)),
                ('width', models.IntegerField(default=70)),
            ],
            options={
                'verbose_name': 'Social Media',
                'verbose_name_plural': 'Social Media',
            },
        ),
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Platform', models.CharField(blank=True, max_length=50, verbose_name='name')),
                ('Username', models.CharField(blank=True, max_length=50)),
                ('url', models.URLField()),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Home',
                'verbose_name_plural': 'Home',
            },
        ),
    ]
