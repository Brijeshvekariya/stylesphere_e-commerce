# Generated by Django 4.2.6 on 2023-11-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_product_product_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='company',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]