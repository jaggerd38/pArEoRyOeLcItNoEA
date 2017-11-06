# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('numero', models.IntegerField()),
                ('modeloavion', models.CharField(max_length=30)),
                ('capacidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Pasajero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Viajar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasajero', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='aerolinea.Pasajero')),
            ],
        ),
        migrations.CreateModel(
            name='Vuelo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aerolinea', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('hora', models.DateTimeField()),
                ('origen', models.CharField(max_length=200)),
                ('destino', models.CharField(max_length=200)),
                ('pasajeros', models.ManyToManyField(through='aerolinea.Viajar', to='aerolinea.Pasajero')),
            ],
        ),
        migrations.AddField(
            model_name='viajar',
            name='vuelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aerolinea.Vuelo'),
        ),
    ]