# Generated by Django 4.2.2 on 2023-06-27 22:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 6, 27, 22, 54, 7, 783217, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='birthday',
            field=models.DateField(default=datetime.datetime(2023, 6, 27, 22, 54, 7, 782217, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]