# Generated by Django 2.2 on 2019-05-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0040_auto_20190520_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='isPublishable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quiz',
            name='isPublishable',
            field=models.BooleanField(default=False),
        ),
    ]
