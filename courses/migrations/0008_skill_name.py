# Generated by Django 4.0.1 on 2022-01-24 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_skill'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='name',
            field=models.CharField(default='my skill', max_length=100),
            preserve_default=False,
        ),
    ]