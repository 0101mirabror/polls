# Generated by Django 4.1.4 on 2022-12-23 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='created_at',
            new_name='created_by',
        ),
    ]
