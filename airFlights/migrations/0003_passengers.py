# Generated by Django 4.1.7 on 2023-03-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airFlights', '0002_airport_alter_flight_flight_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passengers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pass_firstname', models.CharField(max_length=90)),
                ('pass_lastname', models.CharField(max_length=90)),
                ('pass_flight', models.ManyToManyField(blank=True, related_name='passengers', to='airFlights.flight')),
            ],
        ),
    ]
