# Generated by Django 2.2.20 on 2022-01-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_auto_20220106_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='mumber',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]