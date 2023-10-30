# Generated by Django 4.2.6 on 2023-10-22 21:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0007_general_notification_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='general_notification',
            name='user',
        ),
        migrations.AlterField(
            model_name='general_notification',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]