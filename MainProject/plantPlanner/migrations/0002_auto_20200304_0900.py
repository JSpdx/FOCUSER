# Generated by Django 2.2.5 on 2020-03-04 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plantPlanner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='primary_color',
            field=models.CharField(max_length=20),
        ),
    ]