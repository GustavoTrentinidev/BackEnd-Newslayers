# Generated by Django 4.1.1 on 2022-10-13 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_comentario_datacomentario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='datacomentario',
            field=models.DateField(default='2022-10-12'),
        ),
    ]