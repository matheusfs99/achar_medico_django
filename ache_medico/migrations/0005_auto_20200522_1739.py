# Generated by Django 3.0.2 on 2020-05-22 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ache_medico', '0004_auto_20200522_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
