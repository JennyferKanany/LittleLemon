# Generated by Django 4.2.1 on 2023-09-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_alter_menu_inventory_alter_menu_price_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(),
        ),
    ]
