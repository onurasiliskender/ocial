# Generated by Django 2.2 on 2019-04-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0008_remove_topic_courses_total'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='label',
            name='link',
        ),
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
