# Generated by Django 4.2.1 on 2023-07-03 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0019_shifttiming'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlotBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slot_date', models.DateField(auto_now_add=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.extendedusermodel')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gym_app.prefferedtime')),
            ],
        ),
    ]
