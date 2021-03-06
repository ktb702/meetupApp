# Generated by Django 2.2.12 on 2020-06-17 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_name', models.CharField(max_length=255)),
                ('activity_type', models.CharField(max_length=255)),
                ('activity_desc', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'activities',
                'db_table': 'activity',
            },
        ),
        migrations.CreateModel(
            name='MeetUp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meetup_name', models.CharField(max_length=255)),
                ('meetup_date', models.DateField()),
                ('meetup_time', models.TimeField()),
                ('meetup_location', models.CharField(max_length=255)),
                ('meetup_desc', models.CharField(max_length=255)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'meetups',
                'db_table': 'meetup',
            },
        ),
    ]
