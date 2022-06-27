# Generated by Django 4.0.5 on 2022-06-27 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_alter_stationstop_route'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stationstop',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_stops', to='mainapp.route'),
        ),
    ]