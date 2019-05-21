# Generated by Django 2.2 on 2019-05-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0045_course_numberoflearners'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='completeRate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='section',
            name='completeRate',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]