# Generated by Django 5.0.3 on 2024-04-28 21:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_alter_accesorio_nombre'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorio',
            name='nombre_usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='accesorio',
            name='nombre',
            field=models.CharField(choices=[('Caf', 'Cafetera'), ('Pro', 'Proyector'), ('Mic', 'Micrófono'), ('Piz', 'Pizarra')], default='Piz', max_length=3),
        ),
    ]