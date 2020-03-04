# Generated by Django 2.2.5 on 2019-12-06 01:43

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('family', models.CharField(blank=True, max_length=25)),
                ('category', models.CharField(choices=[('Annuals', 'Annuals'), ('Biennials', 'Biennials'), ('Bulbs', 'Bulbs'), ('Cactus/Succulents', 'Cactus/Succulents'), ('Ferns', 'Ferns'), ('Groundcovers', 'Groundcovers'), ('Herbs', 'Herbs'), ('Perennials', 'Perennials'), ('Shrubs', 'Shrubs'), ('Trees', 'Trees'), ('Vegetables', 'Vegetables')], max_length=20)),
                ('genus', models.CharField(max_length=25)),
                ('primary_color', models.CharField(blank=True, max_length=20)),
                ('height', models.CharField(choices=[('under 6in', 'under 6in'), ('6-12in', '6-12in'), ('1-3ft', '1-3ft'), ('4-10ft', '4-10ft'), ('12-20ft', '12-20ft'), ('over 20ft', 'over 20ft')], max_length=20)),
                ('year_sown', models.PositiveIntegerField(blank=True, null=True)),
            ],
            managers=[
                ('Plants', django.db.models.manager.Manager()),
            ],
        ),
    ]