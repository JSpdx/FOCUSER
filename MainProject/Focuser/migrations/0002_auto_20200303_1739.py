# Generated by Django 2.2.5 on 2020-03-04 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Focuser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eclipse',
            name='date',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='eclipse',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='eclipse',
            name='locations',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]