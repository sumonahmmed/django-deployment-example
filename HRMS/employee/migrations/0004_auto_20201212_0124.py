# Generated by Django 3.1.3 on 2020-12-11 19:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0003_auto_20201212_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchdetails',
            name='branch_opening_date',
            field=models.DateField(default=datetime.datetime(2020, 12, 11, 19, 24, 28, 624690, tzinfo=utc), verbose_name='Branch Opening Date'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
