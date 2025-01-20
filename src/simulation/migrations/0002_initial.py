# Generated by Django 5.1.4 on 2025-01-04 18:27

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('simulation', '0001_initial'),
        ('user', '0001_initial'),
        ('vehicle', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='simulationmodel',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_simulation', to='vehicle.categorymodel'),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='person_simulation', to='user.personmodel'),
        ),
        migrations.AddField(
            model_name='simulationmodel',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_simulation', to=settings.AUTH_USER_MODEL),
        ),
    ]
