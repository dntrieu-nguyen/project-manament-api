# Generated by Django 5.1.3 on 2024-12-19 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_projectdocument_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectdocument',
            name='owner',
        ),
    ]
