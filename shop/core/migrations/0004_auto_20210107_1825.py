# Generated by Django 3.1.4 on 2021-01-07 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_product_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='update_at',
            new_name='updated_at',
        ),
    ]
