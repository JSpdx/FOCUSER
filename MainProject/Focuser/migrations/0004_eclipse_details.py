# Generated by Django 2.2.5 on 2020-03-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Focuser', '0003_remove_eclipse_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='eclipse',
            name='details',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
