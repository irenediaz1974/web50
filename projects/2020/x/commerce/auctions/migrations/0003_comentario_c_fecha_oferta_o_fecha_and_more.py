# Generated by Django 4.2.10 on 2024-06-06 10:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_categoria_imagen_producto_subasta_oferta_comentario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='c_fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='oferta',
            name='o_fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_fin',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_ini',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]