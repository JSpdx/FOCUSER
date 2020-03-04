# Generated by Django 2.2.5 on 2020-03-04 01:15

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eclipse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('locations', models.CharField(blank=True, max_length=50)),
                ('type', models.CharField(choices=[('Solar', 'Solar'), ('Lunar', 'Lunar')], max_length=20)),
                ('subtype', models.CharField(choices=[('Penumbral', 'Penumbral'), ('Annular', 'Annular'), ('Total', 'Total'), ('Partial', 'Partial')], max_length=50)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
            ],
            managers=[
                ('Eclipses', django.db.models.manager.Manager()),
            ],
        ),
    ]
