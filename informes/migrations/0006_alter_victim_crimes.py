# Generated by Django 3.2.13 on 2022-05-27 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0005_auto_20220526_1747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='victim',
            name='crimes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.crime'),
        ),
    ]
