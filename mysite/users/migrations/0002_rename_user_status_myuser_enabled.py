# Generated by Django 4.1.4 on 2023-01-02 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='user_status',
            new_name='enabled',
        ),
    ]
