# Generated by Django 4.2.1 on 2023-05-27 07:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('C_H_App', '0006_alter_job_model_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_model',
            name='date_posted',
            field=models.DateTimeField(blank=True, null=True, verbose_name=datetime.datetime(2023, 5, 27, 7, 26, 54, 895967, tzinfo=datetime.timezone.utc)),
        ),
    ]
