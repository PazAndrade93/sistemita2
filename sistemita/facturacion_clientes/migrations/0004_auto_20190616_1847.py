# Generated by Django 2.2.2 on 2019-06-16 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0003_porcentajesaportadosafondosydelivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='porcentajesaportadosafondosydelivery',
            name='porcentaje_delivery',
        ),
        migrations.RemoveField(
            model_name='porcentajesaportadosafondosydelivery',
            name='porcentaje_fondo_administrativo',
        ),
        migrations.RemoveField(
            model_name='porcentajesaportadosafondosydelivery',
            name='porcentaje_fondo_liquido',
        ),
    ]
