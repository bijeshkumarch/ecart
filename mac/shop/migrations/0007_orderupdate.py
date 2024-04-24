# Generated by Django 4.2 on 2023-08-08 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_order_cost'),
    ]

    operations = [
        migrations.CreateModel(
            name='orderUpdate',
            fields=[
                ('order_id', models.IntegerField(default='')),
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('update_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
