# Generated by Django 2.2 on 2019-05-21 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0044_auto_20190521_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='numberofLearners',
            field=models.IntegerField(default=0),
        ),
    ]
