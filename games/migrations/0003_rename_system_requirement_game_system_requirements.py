# Generated by Django 5.2 on 2025-05-21 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_remove_game_system_requirements_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='system_requirement',
            new_name='system_requirements',
        ),
    ]
