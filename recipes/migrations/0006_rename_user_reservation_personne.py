# Generated by Django 4.1.3 on 2022-12-13 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_rename_personne_reservation_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='user',
            new_name='personne',
        ),
    ]
