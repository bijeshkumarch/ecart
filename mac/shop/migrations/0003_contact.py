# Generated by Django 4.2 on 2023-07-14 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=15)),
                ('desc', models.CharField(max_length=500)),
            ],
        ),
    ]