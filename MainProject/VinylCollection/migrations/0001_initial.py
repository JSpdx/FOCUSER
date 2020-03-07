# Generated by Django 2.2.5 on 2020-03-05 19:41

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('artist', models.CharField(max_length=100)),
            ],
            managers=[
                ('Albums', django.db.models.manager.Manager()),
            ],
        ),
    ]