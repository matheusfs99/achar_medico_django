# Generated by Django 3.0.2 on 2020-05-22 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ache_medico', '0002_auto_20200522_1637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medico',
            name='bio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
