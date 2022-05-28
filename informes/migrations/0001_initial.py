# Generated by Django 3.0.7 on 2022-05-26 14:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='crime',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('crime_type', models.CharField(choices=[('Asesinato', 'Asesinato'), ('Robo', 'Robo')], default='Asesinato', max_length=10)),
                ('text', models.TextField()),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('reasons', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='sector',
            fields=[
                ('sector', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('before', models.ImageField(upload_to='images/')),
                ('after', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='victim',
            fields=[
                ('victim', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('year', models.IntegerField()),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('crimes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.crime')),
            ],
        ),
        migrations.CreateModel(
            name='offender',
            fields=[
                ('offender', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('year', models.IntegerField()),
                ('detail', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('crimes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.crime')),
            ],
        ),
        migrations.AddField(
            model_name='crime',
            name='sector',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='informes.sector'),
        ),
    ]
