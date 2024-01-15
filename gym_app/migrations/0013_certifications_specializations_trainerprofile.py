# Generated by Django 4.2.1 on 2023-06-09 05:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gym_app', '0012_attendances'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specializations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainerProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_specializations', models.TextField(blank=True, null=True)),
                ('other_certifications', models.TextField(blank=True, null=True)),
                ('year_of_experience', models.IntegerField(blank=True, null=True)),
                ('education_background', models.TextField(blank=True, null=True)),
                ('certifications', models.ManyToManyField(blank=True, related_name='certifications', to='gym_app.certifications')),
                ('extended_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainer', to='gym_app.extendedusermodel')),
                ('specializations', models.ManyToManyField(blank=True, related_name='specializations', to='gym_app.specializations')),
            ],
        ),
    ]
