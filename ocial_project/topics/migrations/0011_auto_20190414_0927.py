# Generated by Django 2.2 on 2019-04-14 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0010_course_wyl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='wyl',
            new_name='wywl',
        ),
    ]