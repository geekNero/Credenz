# Generated by Django 4.0.4 on 2022-04-15 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rc', '0002_auto_20220311_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='rcplayer',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
