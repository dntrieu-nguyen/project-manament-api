# Generated by Django 5.1.3 on 2024-11-27 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_alter_firebase_tokens_fcm_token'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='task',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='user',
        ),
        migrations.DeleteModel(
            name='Firebase_tokens',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
