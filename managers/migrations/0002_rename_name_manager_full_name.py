# Generated by Django 5.0.4 on 2024-05-08 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='name',
            new_name='full_name',
        ),
    ]