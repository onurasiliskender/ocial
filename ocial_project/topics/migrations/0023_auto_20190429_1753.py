# Generated by Django 2.2 on 2019-04-29 17:53

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0022_course_sectionorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='sectionorder',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=[], size=None),
        ),
    ]