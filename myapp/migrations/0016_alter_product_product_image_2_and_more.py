# Generated by Django 4.2.6 on 2023-11-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_product_product_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image_2',
            field=models.ImageField(upload_to='product_name2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image_3',
            field=models.ImageField(upload_to='product_name3'),
        ),
    ]
