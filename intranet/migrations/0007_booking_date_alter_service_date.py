# Generated by Django 4.2.2 on 2023-06-28 02:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intranet', '0006_alter_service_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='service',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 28, 2, 33, 25, 361066, tzinfo=datetime.timezone.utc)),
        ),
    ]
