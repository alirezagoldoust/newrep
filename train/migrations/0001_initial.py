# Generated by Django 4.2 on 2023-12-15 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=1000)),
                ('phone_number', models.CharField(max_length=20)),
                ('open_time', models.TimeField()),
                ('close_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DurationField()),
                ('no', models.CharField(max_length=20)),
                ('capacity', models.IntegerField()),
                ('price', models.FloatField()),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Des', to='train.station')),
                ('origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='train.station')),
            ],
        ),
    ]
