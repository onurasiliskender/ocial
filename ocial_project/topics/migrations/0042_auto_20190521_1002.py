# Generated by Django 2.2 on 2019-05-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0041_auto_20190520_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='completeRate',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='section',
            name='completeRate',
            field=models.IntegerField(default=0),
        ),
    ]
