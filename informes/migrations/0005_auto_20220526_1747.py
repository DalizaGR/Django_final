# Generated by Django 3.0.7 on 2022-05-26 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0004_auto_20220526_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='crimes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mem_number', to='informes.crime'),
        ),
    ]
