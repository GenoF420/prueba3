# Generated by Django 4.2.2 on 2023-06-28 02:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0005_alter_service_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 28, 2, 32, 58, 302510, tzinfo=datetime.timezone.utc)),
        ),
    ]
