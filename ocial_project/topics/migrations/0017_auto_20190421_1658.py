# Generated by Django 2.2 on 2019-04-21 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0016_auto_20190421_1645'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='name',
            new_name='link',
        ),
    ]
