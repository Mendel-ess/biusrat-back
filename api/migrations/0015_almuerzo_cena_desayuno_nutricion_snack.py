# Generated by Django 5.0.6 on 2024-05-28 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_categoria_popular_recomendado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Almuerzo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Desayuno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Nutricion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=200)),
                ('unit_name', models.CharField(max_length=10)),
                ('value', models.CharField(max_length=10)),
                ('max_value', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Snack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=10)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]