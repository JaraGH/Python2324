# Generated by Django 5.0 on 2023-12-29 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sports', '0002_sport_origin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sport',
            old_name='outdoor',
            new_name='is_outdoor',
        ),
        migrations.RenameField(
            model_name='sport',
            old_name='players',
            new_name='number_players',
        ),
    ]
