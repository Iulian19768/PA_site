# Generated by Django 4.1.3 on 2022-11-28 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradi', '0003_remove_post_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_posted',
        ),
    ]