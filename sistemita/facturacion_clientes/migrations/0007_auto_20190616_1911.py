# Generated by Django 2.2.2 on 2019-06-16 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0006_facturacliente_porcentaje_para_mentoring_sobre_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='facturacliente',
            old_name='porcentaje_para_mentoring_sobre_total',
            new_name='porcentaje_para_mentoring_sobre_total_facturado',
        ),
    ]