# Generated by Django 4.2.1 on 2023-06-01 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0008_alter_ba_status_options_bussinessownermodel_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendedusermodel',
            name='full_name',
            field=models.CharField(default=1, max_length=25),
            preserve_default=False,
        ),
    ]
