# Generated by Django 5.0.3 on 2024-03-04 21:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person_type', models.CharField(choices=[('C', 'Cutter'), ('S', 'Sewer'), ('I', 'Ironer')], max_length=1)),
                ('name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('machine_number', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FabricRoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('weight_or_length', models.CharField(max_length=50)),
                ('fabric_composition', models.CharField(max_length=50)),
                ('arrival_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cutting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('model_name', models.CharField(max_length=100)),
                ('sizes', models.CharField(max_length=50)),
                ('production_date', models.DateField(auto_now_add=True)),
                ('produced_items', models.IntegerField(blank=True, null=True)),
                ('fabric_roll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.fabricroll')),
            ],
        ),
        migrations.CreateModel(
            name='Ironing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ironing_date', models.DateField()),
                ('items_ironed', models.IntegerField()),
                ('cutting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cutting')),
            ],
        ),
        migrations.CreateModel(
            name='Sewing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sewing_date', models.DateField()),
                ('items_produced', models.IntegerField()),
                ('size', models.CharField(max_length=50)),
                ('cutting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.cutting')),
            ],
        ),
    ]
