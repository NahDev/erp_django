# Generated by Django 4.2.4 on 2023-08-02 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_pedido_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('gateway', models.CharField(max_length=100)),
                ('referencia_gateway', models.CharField(blank=True, max_length=100, null=True)),
                ('data_pagamento', models.DateTimeField(blank=True, null=True)),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pedidos.pedido')),
            ],
        ),
    ]
