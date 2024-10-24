# Generated by Django 4.2.10 on 2024-09-19 19:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_producto_id_imagen_imagen_producto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='producto',
        ),
        migrations.AddField(
            model_name='producto',
            name='id_imagen',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_imagen', to='auctions.imagen'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='c_fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 15, 22, 36, 995740, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='o_fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 15, 22, 36, 995740, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 15, 22, 36, 995740, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_ini',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 19, 15, 22, 36, 995740, tzinfo=datetime.timezone.utc)),
        ),
    ]
