# Generated by Django 2.2.3 on 2019-10-10 17:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
