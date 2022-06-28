# Generated by Django 4.0.5 on 2022-06-27 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusStationStop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bus_id', models.IntegerField()),
                ('route_id', models.IntegerField()),
                ('time', models.TimeField()),
            ],
        ),
        migrations.RenameField(
            model_name='stationstop',
            old_name='bus_id',
            new_name='distance_to_next_station',
        ),
        migrations.RenameField(
            model_name='stationstop',
            old_name='route_id',
            new_name='order_number',
        ),
        migrations.RenameField(
            model_name='stationstop',
            old_name='time',
            new_name='time_to_next_station',
        ),
        migrations.RemoveField(
            model_name='route',
            name='distance_between_station',
        ),
        migrations.RemoveField(
            model_name='route',
            name='time_between_station',
        ),
        migrations.AddField(
            model_name='stationstop',
            name='route',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.route'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stationstop',
            name='station',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='mainapp.station'),
            preserve_default=False,
        ),
    ]