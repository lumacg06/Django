# Generated by Django 5.2 on 2025-05-08 18:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0002_producto_fecha_agregado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='fecha_agregado',
        ),
    ]
