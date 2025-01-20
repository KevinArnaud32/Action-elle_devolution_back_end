# Generated by Django 5.1.4 on 2025-01-04 23:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0002_initial'),
        ('vehicle', '0002_remove_vehiclemodel_person'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscriptionmodel',
            name='category',
        ),
        migrations.AddField(
            model_name='subscriptionmodel',
            name='vehicle',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vehicle_subscription', to='vehicle.vehiclemodel'),
            preserve_default=False,
        ),
    ]
