# Generated by Django 5.0.6 on 2024-05-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_usuarios_genero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='fecha_nacimiento',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
