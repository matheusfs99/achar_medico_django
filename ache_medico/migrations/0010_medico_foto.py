# Generated by Django 3.0.2 on 2020-05-25 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ache_medico', '0009_auto_20200525_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='medicos_imgs/'),
        ),
    ]
