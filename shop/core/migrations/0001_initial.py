# Generated by Django 3.1.4 on 2021-01-08 12:05

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', colorfield.fields.ColorField(default='#FF0000', max_length=18)),
                ('title', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.color')),
                ('related', models.ManyToManyField(blank=True, related_name='_product_related_+', to='core.Product')),
                ('sizes', models.ManyToManyField(to='core.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='images')),
                ('product', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.product')),
            ],
        ),
    ]
