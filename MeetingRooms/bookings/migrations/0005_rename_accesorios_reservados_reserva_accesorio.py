# Generated by Django 5.0.3 on 2024-04-24 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_remove_accesorio_fecha_remove_accesorio_sala_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserva',
            old_name='accesorios_reservados',
            new_name='accesorio',
        ),
    ]
