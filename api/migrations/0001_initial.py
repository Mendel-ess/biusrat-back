# Generated by Django 5.0.6 on 2024-05-13 16:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimentacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comida_tiempo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Entrenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_entrenamiento', models.CharField(max_length=50)),
                ('dificultad', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_programa', models.CharField(max_length=50)),
                ('descrip_programa', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Comida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_plato', models.CharField(max_length=50)),
                ('calorias', models.IntegerField()),
                ('cant_proteinas', models.IntegerField()),
                ('cant_grasas', models.IntegerField()),
                ('cant_carbo', models.IntegerField()),
                ('id_alimentacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.alimentacion')),
            ],
        ),
        migrations.CreateModel(
            name='Ejercicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_ejercicio', models.CharField(max_length=50)),
                ('descrip_ejercicio', models.CharField(max_length=150)),
                ('como_hacerlo', models.CharField(max_length=150)),
                ('serie', models.IntegerField()),
                ('repeticion', models.IntegerField()),
                ('peso', models.IntegerField()),
                ('id_entrenamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.entrenamiento')),
            ],
        ),
        migrations.AddField(
            model_name='entrenamiento',
            name='id_programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.programa'),
        ),
        migrations.AddField(
            model_name='alimentacion',
            name='id_programa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.programa'),
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correo', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('genero', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('peso', models.IntegerField()),
                ('altura', models.IntegerField()),
                ('id_programa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.programa')),
            ],
        ),
        migrations.CreateModel(
            name='Sleep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora_acostarse', models.DateTimeField()),
                ('hora_levantarse', models.DateTimeField()),
                ('cant_horas', models.IntegerField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.usuarios')),
            ],
        ),
    ]
