# Generated by Django 3.1.4 on 2021-01-10 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='related',
            field=models.ManyToManyField(blank=True, to='core.Product'),
        ),
    ]