# Generated by Django 5.1.4 on 2025-01-14 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simulation', '0005_simulationmodel_annee_vehicule'),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationmodel',
            name='valeur_neuve',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True),
        ),
    ]
