# Generated by Django 4.2.6 on 2023-12-12 02:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dentist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('phone_number', models.CharField(help_text='eg 240-281-2912', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('phone_number', models.CharField(help_text='eg 240-281-2912', max_length=100, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=150, null=True)),
                ('race', models.CharField(choices=[('American Indian or Alasa Native', 'American Indian or Alasa Native'), ('Asian', 'Asian'), ('Black or African American', 'Black or African American'), ('Hispanic or Latino', 'Hispanic or Latino'), ('Native Hawaiian or Other Pacific islander', 'Native Hawaiian or Other Pacific islander'), ('White', 'White')], max_length=50, null=True)),
                ('gender', models.CharField(choices=[('Male', 'MALE'), ('Female', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('phone_number', models.CharField(help_text='eg 240-281-2912', max_length=100, null=True)),
                ('age', models.IntegerField(null=True)),
                ('adress', models.CharField(max_length=200, null=True)),
                ('dentist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='staff.dentist')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('content', models.CharField(max_length=500, null=True)),
                ('appointment_date', models.DateTimeField(null=True)),
                ('appointment_time', models.TimeField(null=True)),
                ('dentist', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='staff.dentist')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.patient')),
            ],
        ),
    ]
