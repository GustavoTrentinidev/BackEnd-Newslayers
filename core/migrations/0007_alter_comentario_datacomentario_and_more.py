# Generated by Django 4.1.1 on 2022-10-15 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_comentario_datacomentario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='datacomentario',
            field=models.DateField(default='2022-10-15'),
        ),
        migrations.AlterField(
            model_name='midia',
            name='midiapath',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='midia_user',
            name='midiabannerpath',
            field=models.FileField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='midia_user',
            name='midiaprofilepath',
            field=models.FileField(upload_to='media/'),
        ),
    ]
