# Generated by Django 5.0.6 on 2024-05-13 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_ejercicio_como_hacerlo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejercicio',
            name='como_hacerlo',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ejercicio',
            name='descrip_ejercicio',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='programa',
            name='descrip_programa',
            field=models.TextField(),
        ),
    ]