# Generated by Django 4.2.10 on 2024-09-26 11:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0009_alter_comentario_c_fecha_alter_oferta_o_fecha_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subastado',
            name='won_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_won_auctions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comentario',
            name='c_fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 7, 32, 29, 940871, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='oferta',
            name='o_fecha',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 7, 32, 29, 940871, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_fin',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 7, 32, 29, 940871, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='subasta',
            name='s_fecha_ini',
            field=models.DateTimeField(default=datetime.datetime(2024, 9, 26, 7, 32, 29, 940871, tzinfo=datetime.timezone.utc)),
        ),
    ]
