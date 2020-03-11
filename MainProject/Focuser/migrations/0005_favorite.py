# Generated by Django 2.2.5 on 2020-03-11 21:03

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('Focuser', '0004_eclipse_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image_url', models.TextField(max_length=100)),
            ],
            managers=[
                ('Favorites', django.db.models.manager.Manager()),
            ],
        ),
    ]
