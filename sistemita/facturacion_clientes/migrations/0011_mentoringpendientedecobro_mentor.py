# Generated by Django 2.2.2 on 2019-06-19 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facturacion_clientes', '0010_auto_20190619_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentoringpendientedecobro',
            name='mentor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='facturacion_clientes.Consultor'),
            preserve_default=False,
        ),
    ]
