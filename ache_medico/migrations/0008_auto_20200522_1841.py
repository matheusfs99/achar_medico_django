# Generated by Django 3.0.2 on 2020-05-22 21:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ache_medico', '0007_remove_medico_planos_aceitos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ache_medico.Especialidade'),
        ),
    ]
