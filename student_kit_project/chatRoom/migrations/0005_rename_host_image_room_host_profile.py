# Generated by Django 4.2.6 on 2023-11-01 03:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatRoom', '0004_room_host_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='host_image',
            new_name='host_profile',
        ),
    ]