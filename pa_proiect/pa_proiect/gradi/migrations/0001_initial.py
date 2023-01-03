# Generated by Django 4.1.3 on 2022-11-27 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nume', models.CharField(max_length=100)),
                ('prenume', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('numar_tel', models.IntegerField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('adresa', models.CharField(max_length=100)),
                ('codpostal', models.IntegerField(max_length=100)),
                ('content', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
