# Generated by Django 4.1.1 on 2022-09-27 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_midia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='midia_user',
            name='user_iduser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='midia', to=settings.AUTH_USER_MODEL),
        ),
    ]
