# Generated by Django 4.0.1 on 2022-01-24 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_weeklysyllabus_week'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weeklysyllabus',
            name='week',
            field=models.PositiveIntegerField(),
        ),
    ]