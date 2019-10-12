# Generated by Django 2.2.3 on 2019-10-10 16:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_auto_20191010_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rn',
            field=models.IntegerField(blank=True, null=True, unique=True, validators=[django.core.validators.MinValueValidator(1)]),
        ),
    ]
