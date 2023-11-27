# Generated by Django 4.2.6 on 2023-11-25 12:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='company',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pincode',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='seller',
            name='mobile',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.PositiveIntegerField(unique=True),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(choices=[('Mens', 'Mens'), ('Women', 'Women'), ('Kids', 'Kids')], max_length=50)),
                ('product_subcategory', models.CharField(max_length=50)),
                ('product_name', models.CharField(max_length=100)),
                ('product_details', models.TextField()),
                ('product_price', models.PositiveIntegerField()),
                ('product_desc', models.TextField()),
                ('product_image', models.ImageField(upload_to='product_image')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.seller')),
            ],
        ),
    ]