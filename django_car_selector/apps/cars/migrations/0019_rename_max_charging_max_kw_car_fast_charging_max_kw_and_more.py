# Generated by Django 4.0 on 2023-02-26 01:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0018_rename_max_charging_time_max_kw_car_max_charging_max_kw'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='max_charging_max_kw',
            new_name='fast_charging_max_kw',
        ),
        migrations.RenameField(
            model_name='car',
            old_name='max_charging_time',
            new_name='fast_charging_time',
        ),
    ]