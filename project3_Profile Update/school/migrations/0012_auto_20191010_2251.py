# Generated by Django 2.2.3 on 2019-10-10 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_profile_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='skills',
            field=models.TextField(blank=True, null=True),
        ),
    ]
