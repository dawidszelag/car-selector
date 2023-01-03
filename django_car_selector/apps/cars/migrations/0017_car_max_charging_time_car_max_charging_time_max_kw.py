# Generated by Django 4.0 on 2023-01-01 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0016_alter_carbody_options_alter_car_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='max_charging_time',
            field=models.FloatField(blank=True, null=True, verbose_name='Fastcharge time 10%-80%'),
        ),
        migrations.AddField(
            model_name='car',
            name='max_charging_time_max_kw',
            field=models.FloatField(blank=True, null=True, verbose_name='Fastcharge power max KW'),
        ),
    ]