# Generated by Django 2.2.5 on 2019-10-13 19:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('glasses', '0005_auto_20191013_1854'),
    ]

    operations = [
        migrations.AddField(
            model_name='glass',
            name='creation_moment',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
