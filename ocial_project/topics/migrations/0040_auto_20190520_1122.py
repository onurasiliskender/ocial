# Generated by Django 2.2 on 2019-05-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0039_auto_20190519_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='isPublishable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='isPublishable',
            field=models.BooleanField(default=False),
        ),
    ]
