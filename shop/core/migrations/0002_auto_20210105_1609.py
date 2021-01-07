# Generated by Django 3.1.5 on 2021-01-05 16:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='color',
            name='title',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('discount', models.PositiveIntegerField(blank=True, null=True)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.color')),
                ('photos', models.ManyToManyField(to='core.Photo')),
                ('related', models.ManyToManyField(blank=True, related_name='_product_related_+', to='core.Product')),
                ('sizes', models.ManyToManyField(to='core.Size')),
            ],
        ),
    ]