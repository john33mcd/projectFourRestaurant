# Generated by Django 3.2.18 on 2023-04-21 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField()),
            ],
        ),
    ]
