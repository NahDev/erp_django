# Generated by Django 4.2.4 on 2023-08-09 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logistica', '0003_veiculo_placa'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veiculo',
            old_name='nome',
            new_name='empresa',
        ),
    ]
