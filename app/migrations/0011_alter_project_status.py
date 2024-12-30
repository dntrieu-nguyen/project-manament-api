# Generated by Django 5.1.3 on 2024-12-30 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in-progress', 'In Progress'), ('completed', 'Completed'), ('open', 'Open'), ('close', 'Close')], default='pending', max_length=50),
        ),
    ]
