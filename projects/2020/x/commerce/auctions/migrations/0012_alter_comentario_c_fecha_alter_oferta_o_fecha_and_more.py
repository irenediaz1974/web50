# Generated by Django 4.2.10 on 2024-09-27 10:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_remove_comentario_id_subasta_comentario_id_producto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='c_fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 6, 47, 2, 135675, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='o_fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 6, 47, 2, 135675, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 6, 47, 2, 135675, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_ini',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 27, 6, 47, 2, 135675, tzinfo=datetime.timezone.utc)),
        ),
    ]
