# Generated by Django 4.2.1 on 2023-09-27 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_alter_booking_no_of_guests'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='menu',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='booking',
            name='bookingDate',
            field=models.DateTimeField(),
        ),
    ]