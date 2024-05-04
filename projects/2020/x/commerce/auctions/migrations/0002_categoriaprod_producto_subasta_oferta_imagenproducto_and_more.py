# Generated by Django 4.2.10 on 2024-05-04 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('precio_inicial', models.FloatField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='auctions.categoriaprod')),
            ],
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('descripcion', models.TextField()),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('estado', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Oferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monto', models.FloatField()),
                ('subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subasta', to='auctions.subasta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='ruta/donde/guardar/imagenes')),
                ('descripcion', models.TextField()),
                ('id_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.producto')),
            ],
        ),
        migrations.CreateModel(
            name='ComentarioSubasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarioSubasta', to='auctions.subasta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ComentarioUsuario', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subastado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='producto_sub', to='auctions.producto')),
                ('subasta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subastado', to='auctions.subasta')),
            ],
            options={
                'unique_together': {('subasta', 'producto')},
            },
        ),
    ]
