# Generated by Django 3.2.9 on 2023-07-10 06:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0026_prefferedtime_reset_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prefferedtime',
            name='reset_date',
            field=models.DateField(default=datetime.date(2023, 7, 10)),
        ),
        migrations.AlterField(
            model_name='slotbooking',
            name='slot_date',
            field=models.DateField(),
        ),
    ]
