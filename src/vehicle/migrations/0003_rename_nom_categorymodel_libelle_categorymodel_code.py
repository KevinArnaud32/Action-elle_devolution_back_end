# Generated by Django 5.1.4 on 2025-01-11 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_remove_vehiclemodel_person'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categorymodel',
            old_name='nom',
            new_name='libelle',
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='code',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
