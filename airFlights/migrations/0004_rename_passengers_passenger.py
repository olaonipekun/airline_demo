# Generated by Django 4.1.7 on 2023-03-24 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airFlights', '0003_passengers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passengers',
            new_name='Passenger',
        ),
    ]
